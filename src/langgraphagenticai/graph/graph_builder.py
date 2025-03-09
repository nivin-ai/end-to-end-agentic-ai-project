from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
import streamlit as st

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def build_basic_chatbot_graph(self):
        '''
        builds a basic chatbot graph
        this method simply initializes a BasicChatbotNode class
        '''
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("basic_chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "basic_chatbot")
        self.graph_builder.add_edge("basic_chatbot", END)

    def setup_graph(self, usecase: str):
        '''
        sets up the graph for a specific use case
        '''
        if usecase=="Basic Chatbot":
            self.build_basic_chatbot_graph()
        # Debugging: Print the graph structure before compiling
        st.write(f"Nodes in graph: {self.graph_builder.nodes}")
        st.write(f"Edges in graph: {self.graph_builder.edges}")
        return self.graph_builder.compile()
    
