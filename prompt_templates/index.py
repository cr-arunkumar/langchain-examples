from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define the system message
system_message = SystemMessage(content="""
You are an expert cold email writer with 35 years of experience. 
Your task is to write a professional and compelling cold email for job applications.
Ensure the email is concise, highlights the applicant's relevant skills, and expresses genuine interest in the company.
""")

# Define the human message template
human_template = """Write a cold email for a job application with the following details:
- Recipient: {recipient_name}
- Sender: {sender_name}
- Position: {position}
- Company: {company}
- Industry: {industry}
- Relevant Experience: {relevant_experience}    
- Reason for Interest: {reason_for_interest}
- Sender Contact Info: {sender_contact_info}

The email should be professional, concise, and tailored to the specific job and company.
"""

# Create the ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages([system_message ,human_template])

# Prepare the prompt
prompt = prompt_template.format_messages(
    recipient_name="John Doe",
    sender_name="Jane Smith",
    position="Software Engineer",
    company="Creole Studios",
    industry="Technology",
    relevant_experience="5 years in software development",
    reason_for_interest="I admire your commitment to innovation and quality.",
    sender_contact_info="jane.smith@email.com"
)

# Send the prompt to the LLM
response = llm.invoke(prompt)

# Print the response
print("\n\n--------------------------------\n\n")
print(f"Response:\n{response.content}")