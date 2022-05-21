import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import requests
from streamlit_lottie import st_lottie
import json

def app():


    def load_lottiefile (filepath: str):
     
        with open (filepath, "r") as f :
         return json.load(f) 

    lottie_robot = load_lottiefile("lottiefiles/robot.json")

    left_column , right_column = st.columns(2)

    with right_column:

      st_lottie(lottie_robot, height=300, width=300, key="doctor")


    st.title('Explore')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)

    
