from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatMessagePromptTemplate
from dotenv import load_dotenv 


load_dotenv()

Chat_model = ChatGroq(model = "openai/gpt-oss-20b" , temperature=0.5)

