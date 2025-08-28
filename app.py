import streamlit as st
import numpy as np

st.set_page_config(page_title="Doctoral Diabetes Checker", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
    body {background: linear-gradient(135deg, #cceeff, #e6f7ff); color: #003366; font-family: 'Arial', sans-serif;}
    .stButton>button {background-color: #0066cc; color: white; border-radius: 12px; padding: 0.6em 1.2em; font-size: 16px; transition: 0.3s;}
    .stButton>button:hover {background-color: #004080; transform: scale(1.05);}
    </style>
""", unsafe_allow_html=True)

st.title("🩺 Doctoral Diabetes Prediction Platform")
st.markdown("### Enter patient details below to check diabetes risk.")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20)
glucose = st.number_input("Glucose Level", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("🔍 Predict"):
    if glucose > 125 or bmi > 30:
        st.error("⚠️ High chance of Diabetes — consult a doctor.")
    else:
        st.success("✅ Low chance of Diabetes — stay healthy!")
