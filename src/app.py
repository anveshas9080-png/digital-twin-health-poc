import streamlit as st
import pandas as pd

st.title("Digital Twin Health PoC")
st.write("Simulating lifestyle inputs against health risk trajectories.")

# User Input Sliders
age = st.slider("Age", 20, 80, 30)
bmi = st.slider("BMI", 15.0, 40.0, 22.5)
glucose = st.slider("Fasting Glucose Level (mg/dL)", 70, 200, 100)

# Simple Predictive Logic
risk_score = (glucose * 0.4) + (bmi * 1.5) + (age * 0.2)

st.subheader("Simulated Health Output")
if risk_score > 120:
    st.error(f"Elevated Risk Trajectory (Score: {risk_score:.1f}). Recommended lifestyle intervention.")
else:
    st.success(f"Stable Health Trajectory (Score: {risk_score:.1f}). Normal metabolic range.")
