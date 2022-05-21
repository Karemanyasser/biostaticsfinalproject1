import streamlit as st
from multiapp import MultiApp
from apps import welcome, explore, predicte # import your app modules here

app = MultiApp()

st.markdown("""
# Diabetes Prediction 

We will be predicting that whether the patient has diabetes or not, on the basis of the features he will provide to our machine learning model.
""")


# Add all your application here
app.add_app("Welcome", welcome.app)
app.add_app("Explore", explore.app)
app.add_app("Predicte", predicte.app)
# The main app
app.run()
