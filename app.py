import streamlit as st
import joblib

# Load the model
model = joblib.load('stacking_model.pkl')

# Streamlit app
st.title("Sales Forecasting App")
features = st.text_input("Enter features separated by commas")

if st.button("Predict"):
    features_list = [float(i) for i in features.split(',')]
    prediction = model.predict([features_list])
    st.write(f"Predicted Sales: {prediction[0]}")
