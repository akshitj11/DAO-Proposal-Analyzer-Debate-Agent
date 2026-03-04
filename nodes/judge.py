from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from state import State
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an impartial judge evaluating a DAO governance debate. 
You will be given arguments for and against a proposal. 
Analyze both sides and respond in exactly this format:
Verdict: <your vote recommendation and why in 2-3 sentences>
Confidence: <number out of 10>"""),
    ("human", "Advocate argues: {advocate_argument}\nCritic argues: {critic_argument}")
])

chain = prompt | model
def judge_node(state:State):
    response = chain.invoke({
        "advocate_argument":state["advocate_argument"],
        "critic_argument":state["critic_argument"]})
      #parsing the output

    lines = response.content.strip().split("\n")
    verdict = lines[0].replace("Verdict:","").strip()
    confidence = int(lines[1].replace("Confidence","").strip())

    return {
    "verdict":verdict,
    "confidence":confidence,
    "round":state["round"]+1
     }