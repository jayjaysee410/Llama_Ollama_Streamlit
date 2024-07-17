from langchain_community.llms import Ollama 
import streamlit as st

llm = Ollama(model="llama3")

st.title("Chatbot using Llama3")

prompt = st.text_area("Enter your prompt/question:")
 
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            #st.write_stream(llm.invoke(prompt, stop=['<|eot_id|>']))
            st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))


# print(llm.invoke("Tell me a short joke", stop=['<|eot_id|>']))