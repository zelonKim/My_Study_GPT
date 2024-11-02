import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.schema.runnable import RunnablePassthrough
from langchain.callbacks.base import BaseCallbackHandler


st.set_page_config(
    page_title="Voca GPT",
    page_icon="📙",
)


st.title("Voca GPT")


st.markdown("""
    This is English Dictionary.
    Input the English vocabulary that you want to search.
""")




#########################




llm = ChatOpenAI(
    temperature=0.1,
    model="gpt-3.5-turbo-1106",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)


prompt = ChatPromptTemplate.from_template(
         """
            You are an first-class English-Korean Dictionary.
            Please Explain the {voca} with example sentence.
            And also, explain in Korean with translating naturally.
            print the Result like the below.

                - meaning : 

                - Example Sentence :

            -----------------------------------------------

                * 뜻 :

                * 예문 :
        """
)


chain = ({"voca": RunnablePassthrough()} | prompt | llm)




#####################



inputVoca = st.text_input("Search:", placeholder="영단어를 입력하세요.")

if inputVoca:
    outputVoca = chain.invoke(inputVoca)
    st.write(outputVoca.content)