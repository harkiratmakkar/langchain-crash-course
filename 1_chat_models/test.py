from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

chat_history = []
chat_history.append(SystemMessage("You are a helpful assistant"))

while True:
    human_in = input('You: ')
    if human_in.lower() == 'bye':
        break

    chat_history.append(HumanMessage(human_in))

    model_result = model.invoke(chat_history)
    response = model_result.content
    chat_history.append(HumanMessage(response))
    print(f"AI: {response}")