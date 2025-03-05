import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model_path = "final.pkl"

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    st.error("Model file not found! Please upload 'model.pkl'.")

# Title and Introduction
st.title("Heart Failure Readmission Prediction")
st.write("This app predicts whether a heart failure patient will be readmitted within 30 days.")

# Input Fields
age = st.number_input("Age", min_value=20, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
heart_rate = st.number_input("Heart Rate", min_value=50, max_value=200, step=1)
blood_pressure = st.number_input("Blood Pressure", min_value=80, max_value=200, step=1)
blood_sugar = st.number_input("Blood Sugar", min_value=50, max_value=300, step=1)
ck_mb = st.number_input("CK-MB Level", min_value=0.0, max_value=50.0, step=0.1)
troponin = st.number_input("Troponin Level", min_value=0.0, max_value=10.0, step=0.1)

# Convert categorical input
gender = 1 if gender == "Male" else 0

# Predict Button
if st.button("Predict"):
    if model:
        input_data = np.array([[age, gender, heart_rate, blood_pressure, blood_sugar, ck_mb, troponin]])
        prediction = model.predict(input_data)
        result = "Likely to be readmitted" if prediction[0] == 1 else "Unlikely to be readmitted"
        st.success(f"Prediction: {result}")
    else:
        st.error("Model not loaded. Train and save the model first.")


