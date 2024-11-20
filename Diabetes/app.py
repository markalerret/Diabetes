import streamlit as st
import pandas as pd

#run these commands in command prompt to open app in browser
#cd C:\Users\mark\Desktop\Coding Projects\Diabetes
#python -m streamlit run app.py

#text for streamlit app
st.write("""
# Insulin Dose Calculator
""")

#streamlit inputs
blood_sugar_reading_result = st.number_input("Blood Sugar Reading Result")
target_blood_sugar = st.number_input("Target Blood Sugar")
individual_insulin_sensitivity = st.number_input("Individual Insulin Sensitivity")
carbs_per_serving = st.number_input("Carbs per Serving")
number_of_servings = st.number_input("Number of Servings")
carbs_to_units_ratio = st.number_input("Carbs to Units Ratio")

#calculation function
def units_to_pump(blood_sugar_reading_result, target_blood_sugar, individual_insulin_sensitivity, carbs_per_serving, number_of_servings, carbs_to_units_ratio):
    units_to_pump = (blood_sugar_reading_result - target_blood_sugar) / individual_insulin_sensitivity + (carbs_per_serving * number_of_servings / carbs_to_units_ratio)
    return units_to_pump

if st.button("Calculate"):
    result = units_to_pump(blood_sugar_reading_result, target_blood_sugar, individual_insulin_sensitivity, carbs_per_serving, number_of_servings, carbs_to_units_ratio)
    st.write(result, "units")

#example of function
#units_to_pump(193, 140, 50, 29, 2.5, 10)
