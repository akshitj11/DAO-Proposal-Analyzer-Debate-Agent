from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from state import State
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strong critic for DAO proposals. Given a proposal, build the strongest possible case in againt of it. Be persuasive, concise, and focus on risks and concerns regarding it."),
    ("human","proposal:{proposal}")
])

chain = prompt | model

def critic_node(state : State):
    response = chain.invoke ({"proposal":state["proposal"]})
    return{"critic_argument":response.content }

