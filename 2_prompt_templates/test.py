from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

template = ChatPromptTemplate.from_messages([
    ('system',"You are the best maths teacher."),
    ('human',"Solve x + 3 = 4"),
    ('ai',r''' 
                Step 1: Take all numerical values on one side of the equation; x = 4 - 3.
                Step 2: Solve for x; x = 1
                '''),
    ('human','Solve x + {num_1} = {num_2}')
    ])
num_1_in = int(input("Enter the first number: "))
num_2_in = int(input("Enter the second number: "))
prompt = template.invoke({
    'num_1':num_1_in,
    'num_2':num_2_in,
})

print(prompt)
model = ChatOpenAI(model="gpt-4o")
model_result = model.invoke(prompt)
response = model_result.content
print(response)