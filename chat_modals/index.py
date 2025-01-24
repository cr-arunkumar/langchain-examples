from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
load_dotenv()

# Initialize the GroQ chatbot
llm=ChatGroq(model="llama-3.3-70b-versatile")


def simple_llm():
    question = "What is square root of 49"
    answer = llm.invoke(question)
    # Print the answer
    print(f"Answer: {answer}")


def with_converstion():
    messages=[
        SystemMessage(content="You are a senior Full stack developer with 20 years of experience"),
        AIMessage(content="I am familiar with Nextjs,Python,AI/ML, Node.js, Tailwindcss, React.js and etc."),
    ]

    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            break
        messages.append(HumanMessage(content=user_message))
        answer = llm.invoke(messages)
        messages.append(AIMessage(content=answer.content))
        print(f"Me: {answer.content}")

with_converstion()

