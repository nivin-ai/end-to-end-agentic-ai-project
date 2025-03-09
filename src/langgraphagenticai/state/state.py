from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    ''''
    Represents the structure of state used in the graph.
    '''
    messages = Annotated[list, add_messages]