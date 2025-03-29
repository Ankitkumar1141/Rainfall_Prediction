import pandas as pd
import numpy as np
import streamlit as st
import pickle

## Load the xgboost model
with open ("xgboost_best_model.pkl","rb") as file:
    model = pickle.load(file)

## Title for model
st.title("Rainfall Prediction App")

## Sidebar for user inputs
st.sidebar.header("Input features")

## Creating function for user input
def user_input_features():
    pressure = st.sidebar.slider("Pressure (hPa)",900.0,1100.0,1013.0)
    dewpoint = st.sidebar.slider("Dew Point (%)",0.0,30.0,21.0)
    humidity = st.sidebar.slider("Humidity (%)",50,110,80)
    cloud = st.sidebar.slider("Cloud",5,105,80)
    sunshine = st.sidebar.slider("Sunshine",0.0,15.0,3.5)
    winddirection = st.sidebar.slider("Wind direction",5.0,360.0,70.5)
    windspeed = st.sidebar.slider("Wind speed (m/s)",2.0,54.0,20.500)
    data = {
        "Pressure" : [pressure],
        "Dew point" : [dewpoint],
        "Humidity" : [humidity],
        "Cloud" : [cloud],
        "Sunshine" : [sunshine],
        "Wind direction" : [winddirection],
        "Wind speed" : [windspeed]
    }
    return pd.DataFrame(data)

input_df = user_input_features()

## Display user inputs
st.write("Entered input features")
st.write(input_df)

## Prediction
if st.button ("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success("Rain is predicted !")
    else:
        st.success("No Rain is predicted")

## Footer
st.write("---")
st.write("Developed by Ankit kumar")

