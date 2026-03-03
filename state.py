from typing import TypedDict

class state(TypedDict):
    proposal: str
    advocate_argument:str
    critic_argument:str
    verdict:str
    confidence: int
    round:int
    