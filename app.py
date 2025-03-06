import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), r"final.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    st.error("🚨 Model file not found!")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2c3e50;
        }
        .sub-title {
            font-size: 20px;
            text-align: center;
            color: #34495e;
        }
        .stButton>button {
            background-color: #2ecc71;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #27ae60;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown('<h1 class="main-title">🫀 Heart Failure Readmission Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Predict if a heart failure patient is likely to be readmitted within 30 days 🏥</p>', unsafe_allow_html=True)
st.write("---")

# Sidebar for Info
st.sidebar.title("ℹ️ About This App")
st.sidebar.write("This AI-powered app helps predict **heart failure readmission** based on vital patient data. It uses a machine learning model trained on real patient records.")

# Input Fields Layout
col1, col2 = st.columns(2)

with col1:
    age_at_admission = st.number_input("🧑‍⚕️ Age at Admission", min_value=20, max_value=100, step=1)
    hadm_id = st.number_input("🏥 Hospital Admission ID", min_value=100000, max_value=999999, step=1)
    systolic_bp = st.number_input("❤️ Systolic BP", min_value=80, max_value=200, step=1)

with col2:
    diastolic_bp = st.number_input("💙 Diastolic BP", min_value=50, max_value=150, step=1)
    spo2 = st.number_input("🫁 Oxygen Saturation (SpO2)", min_value=50, max_value=100, step=1)
    glucose = st.number_input("🩸 Blood Glucose Level", min_value=50, max_value=300, step=1)

aspirin = st.checkbox("💊 Taking Aspirin?")  # Binary Feature
aspirin = 1 if aspirin else 0

st.write("---")

# Predict Button with Styling
if st.button("🔍 Predict Readmission"):
    if model:
        input_data = np.array([[age_at_admission, hadm_id, systolic_bp, diastolic_bp, spo2, glucose, aspirin]])
        prediction = model.predict(input_data)
        result = "✅ Likely to be readmitted" if prediction[0] == 1 else "❌ Unlikely to be readmitted"
        st.success(f"**Prediction:** {result}")
    else:
        st.error("❌ Model not loaded. Train and save the model first.")

st.write("---")
