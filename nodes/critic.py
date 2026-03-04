from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from state import State
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strong critic for DAO proposals. Given a proposal, build the strongest possible case in againt of it. Be persuasive, concise, and focus on risks and concerns regarding it."),
    ("human","proposal:{proposal}")
])

chain = prompt | model

def critic_node(state : State):
    response = chain.invoke ({"proposal":state["proposal"]})
    return{"critic_argument":response.content }

