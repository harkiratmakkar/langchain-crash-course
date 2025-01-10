# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

messeges = [
    SystemMessage("You are the best math problem solver"),
    HumanMessage("What is 2 + 3 - 5 * 9"),
    AIMessage("Using BODMAS, we solve multiply first which gives us 2 + 3 - 45. Then we solve addition \
              which gives us 5 - 45. So, the final result is -40."),
    HumanMessage("What is 6 - 8 + 9 - 5 * 3 / 4")
]
# Invoke the model with a message
result = model.invoke(messeges)
print(result.content)

