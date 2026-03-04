from typing import TypedDict

class State(TypedDict):
    proposal: str
    advocate_argument:str
    critic_argument:str
    verdict:str
    confidence: int
    round:int
    