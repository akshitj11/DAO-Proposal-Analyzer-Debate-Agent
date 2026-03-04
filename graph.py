from langgraph.graph import StateGraph, END
from state import State
from nodes.advocate import advocate_node
from nodes.critic import critic_node
from nodes.judge import judge_node

graph = StateGraph(State)


graph.add_node("advocate", advocate_node)
graph.add_node("critic", critic_node)
graph.add_node("judge", judge_node)

graph.add_edges("advocate","critic")
graph.add_edge("critic","judge")

def should_loop(state:State):
    if state["round"] >= 3:
        return END
    if state["confidence"] >= 7:
        return END
    return "advocate"

graph.add_conditional_edges("judge",should_loop)

graph.set_entry_point("advocate")
app=graph.compile()