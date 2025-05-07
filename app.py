import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.title("🏢 Building Sustainability Classifier")
st.markdown("Enter the building features below to predict if it's **sustainable** 🌱 or not ❌.")

# Input sliders
co2 = st.slider("CO2 emissions", 50, 300, 150)
energy = st.slider("Energy use", 2000, 10000, 5000)
size = st.slider("Building size", 50, 200, 100)

# Predict button
if st.button("Predict Sustainability"):
    input_df = pd.DataFrame([[co2, energy, size]], columns=['CO2_emissions', 'energy_use', 'building_size'])
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ This building is likely **SUSTAINABLE**.")
    else:
        st.error("❌ This building is likely **NOT sustainable**.")
