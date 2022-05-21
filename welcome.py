from turtle import right
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json


def app():
    st.title('Getting Started')

    st.write('from the Main Menu')

    st.write('please choose your request')


    def load_lottiefile (filepath: str):
     
        with open (filepath, "r") as f :
         return json.load(f) 

    lottie_welcome = load_lottiefile("lottiefiles/welcome.json")

    lottie_machine = load_lottiefile("lottiefiles/machine.json")


    left_column , right_column = st.columns(2)

    with right_column:

      st_lottie(lottie_welcome, height=300, width=300, key="welcome")

    with left_column:

      st_lottie(lottie_machine, height=300, width=300, key="machine")
 