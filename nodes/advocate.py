from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from state import state
from dotenv import load_dotenv
import os
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strong advocate for DAO proposals. Given a proposal, build the strongest possible case in favor of it. Be persuasive, concise, and focus on community benefit, growth, and value."),
    ("human","proposal:{proposal}")
])

chain = prompt | model

def advocate_node(state : State):
    response = chain.invoke ({"proposal":state["proposal"]})
    return{"advocate_argument":response.content }

