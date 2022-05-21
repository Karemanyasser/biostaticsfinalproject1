import threading
import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import requests
from streamlit_lottie import st_lottie
import json
import pickle
import numpy as np
from imp import load_module

def app (): 

    def load_model () :
        with open ('clf.pkl', 'rb') as pickle_in:
             clf = pickle.load(pickle_in)
        return clf
    
    clf = load_model()

    Age = st.number_input('Insert your age')

    Weight = st.number_input('Insert your weight')
 
    Cholesterol = st.number_input('Insert your Cholesterol level')

    Bmi = st.number_input('Insert body mass index (BMI)')

    Glucose = st.number_input('Insert your Glucose level')

    Hdl_chol = st.number_input('Insert high-density lipoprotein cholesterol')

    Chol_hdl_ratio = st.number_input('Insert ')

    Systolic_bp = st.number_input('Insert systolic blood pressure')

    Diastolic_bp = st.number_input('Insert diastolic blood pressure')

    Waist_hip_ratio = st.number_input('Insert waist to hip ratio')

    ok = st.button ("Start prediction")    

    def prediction(cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, weight, bmi, systolic_bp, diastolic_bp, waist_hip_ratio):
        prediction = clf.predict(
            [[cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, weight, bmi, systolic_bp, diastolic_bp, waist_hip_ratio]])        
        return(prediction)
    if ok :
         st.subheader(f"the patient has",prediction(Cholesterol,Glucose,Hdl_chol,Chol_hdl_ratio,Age,Weight,Bmi,Systolic_bp,Diastolic_bp,Waist_hip_ratio))



        #!------loading the animation----------
 
         def load_lottiefile (filepath: str):
     
          with open (filepath, "r") as f :
           return json.load(f) 

         lottie_doctor = load_lottiefile("lottiefiles/doctor.json")

         left_column , right_column = st.columns(2)

         with right_column:

          st_lottie(lottie_doctor, height=300, width=300, key="doctor")    






# *def app():
#  *   st.title('Predicte')

#   *  st.write('This is the `Predication` page. Enter your data')


    # Load iris dataset
    #* iris = datasets.load_iris()
    # *X = iris.data
    # *Y = iris.target

    # Model building
    # *st.header('Model performance')
    #* X_train, X_test, Y_train, Y_test = train_test_split(
    # *    X, Y, test_size=0.2, random_state=42)
    # *clf = RandomForestClassifier()
    # *clf.fit(X_train, Y_train)
    # *score = clf.score(X_test, Y_test)
    # *st.write('Accuracy:')
    # *st.write(score)




