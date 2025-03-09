from src.langgraphagenticai.state.state import State
import streamlit as st

class BasicChatbotNode:
    '''
    basic chatbot logic implementation
    '''
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        '''
        processes the input and returns an output
        '''
        st.write(f"state: {state}")
        #return {"messages": self.llm.invoke(state['messages'])}
        return {"messages": "hi there"}