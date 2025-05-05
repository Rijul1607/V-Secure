import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load(r"C:\Users\RIJUL GULATI\Downloads\random_forest_modelnew.pkl")

# Label mapping (numeric to label)
label_map = {0: 'Flooding', 1: 'Fuzzing', 2: 'Normal', 3: 'Replay', 4: 'Spoofing'}

st.title("CAN Message Classifier")

st.markdown("Enter CAN message details below. The number of `Byte_i` fields will adjust based on the DLC value.")

# User inputs
arbitration_id = st.number_input("Arbitration ID", min_value=0, step=1)
dlc = st.slider("DLC (Data Length Code)", min_value=0, max_value=8, step=1)

# Dynamic Byte inputs based on DLC
byte_values = []
for i in range(dlc):
    byte_val = st.number_input(f"Byte_{i}", min_value=0, max_value=255, step=1)
    byte_values.append(byte_val)

# Fill remaining bytes with -1 (as used in training)
for _ in range(8 - dlc):
    byte_values.append(-1)

# Predict button
if st.button("Predict Attack Type"):
    features = [arbitration_id, dlc] + byte_values
    prediction = model.predict([features])[0]
    predicted_label = label_map.get(prediction, "Unknown")
    
    if predicted_label == "Normal":
        st.markdown(f"<h3 style='color:green;'>✅ No Attack: {predicted_label}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color:red;'>🚨 Attack: {predicted_label}</h3>", unsafe_allow_html=True)
