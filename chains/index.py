from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system"),"You are a senior Full stack developer with 20 years of experience build scalable applications.You only provide ans for the technical questions related to your field. For more information",
        ("human","Write a code  {techincal_question}"),
    ]
)

# Create the combined chains using lang chain expression  syntax
chain=prompt_template | llm | StrOutputParser()

# Execute the chain and get the result
response = chain.invoke({
  "techincal_question":"fetch data from a REST API using Typescript and axios requests library. Include error handling and logging in the code."
})

print(response)