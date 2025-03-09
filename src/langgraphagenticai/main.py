import streamlit as st
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


# MAIN function start
def load_langgraph_agentic_ai():
    '''
    loads and runs the langgraph agentic ai application
    this function loads the streamlit ui, handles user input, sets up the llm and graph,
    and displays the output while handling exception cases to ensure robustness
    '''
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Failed to load user input from UI")
        return
    
    #text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")
    
    if user_message:
        try:
            #configure llm
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Model could not be initialized.")
                return
            
            #initialize and set up the graph based on the use case
            use_case = user_input.get("selected_usecase")
            graph_builder = GraphBuilder(model=model)
            try:
                st.write(f"use caes: {use_case}")
                graph = graph_builder.setup_graph(use_case)
                st.write("Graph setup done")
                DisplayResultStreamlit(usecase=use_case, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Failed to build graph with exception {e}")
                return
        except Exception as e:
            st.write(f"Exception - {e}")
