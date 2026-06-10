from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import ToolNode, tools_condition
import logging

logger = logging.getLogger(__name__)


GameOver: bool = False

class TriviaState(MessagesState):
    score: int
    questions_asked: int


llm = ChatOllama(model="qwen3.5:4b")
#-------------------- Tools ---------------------#
def record_score(points: int):
    """
    This tool is to record a point if the user answered a question correctly or not 
    If the answer is correct the points is 1 if it is wrong the point is 0
    """
    current_score = int(TriviaState["score "]) + points
    TriviaState["score"] = current_score
    return TriviaState["score"]

def isGameOver(state: TriviaState, game_state: bool = False):
    """
    if all 5 of the trivia questions have been asked and the final score has been returned to the user then set game_state to True to end
    the game.
    """
    global GameOver
    GameOver = game_state

tools = [record_score]
llm_with_tools = llm.bind_tools(tools)


#----------------- Nodes -------------------------#
def assistant(state: TriviaState):
    system_prompt = """You are a trivia host your job is to ask 5 trivia questions with a specific set of multiple choice options for the user to pick from and track the points they gain each correct answer is
    one point once you have asked them 5 questions you should end it and let them know their score out of 5"""
    response = llm_with_tools.invoke([SystemMessage(system_prompt)] + state["messages"])
    return {"messages": [response]}



#--------------- Graph Building -------------------#
builder = StateGraph(TriviaState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Add edge conditons
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("assistant", "tools")

graph = builder.compile()

#--------------- Game Play -----------------------#

def call_llm():
    user_message = input("What is your answer?")
    response = graph.invoke({"messages": [HumanMessage(user_message)]})
    return print(response["messages"][-1].content)
