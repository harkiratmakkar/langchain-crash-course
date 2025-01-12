from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

prompt_template = ChatPromptTemplate.from_messages([
    ('system','You are a helpful assistant'),
    ('human','Classify the following feedback as positive, negative or neutral. Return only the label. Feedback: This product was awesone'),
    ('ai','positive'),
    ('human','Feedback: {feedback}'),
])

model = ChatOpenAI(model="gpt-4o")

def positive_feedback_func(x):
    model = ChatOpenAI(model="gpt-4o")
    return model.invoke('Create a 20 word thank you note for a customer.').content

def negative_feedback_func(x):
    model = ChatOpenAI(model="gpt-4o")
    return model.invoke('Create a 20 word sorry note for a customer.').content

def neutral_feedback_func(x):
    return "Thanks. Hope to serve you again."

branches = RunnableBranch(
    (lambda x: x == 'positive', lambda x: positive_feedback_func(x)),
    (lambda x: x == 'negative', lambda x: negative_feedback_func(x)),
    (lambda x: x == 'neutral', lambda x: neutral_feedback_func(x)),
    lambda x: f"Not sure about the response from model: {x}"
)

chain = prompt_template | model | StrOutputParser() | branches

review = "The product is just pure shit."
result = chain.invoke({"feedback": review})
print(result)

# print(branches.invoke(model.invoke(prompt_template.invoke({"feedback": review})).content))
