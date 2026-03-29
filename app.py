import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("💧 Water Quality Analyzer")

st.write("Enter water parameters:")

# Inputs
ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
solids = st.number_input("TDS", 0.0, 50000.0, 10000.0)
chloramines = st.number_input("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0, 250.0)
conductivity = st.number_input("Conductivity", 0.0, 1000.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 10.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 200.0, 80.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

# Button
if st.button("Check Water Quality"):

    # Message
    st.write("🔍 Checking water quality using trained ML model...")

    # Prepare input
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon,
                            trihalomethanes, turbidity]])

    # Prediction
    prediction = model.predict(input_data)

    # Result
    if prediction[0] == 1:
        st.success("✅ Water is SAFE to drink")
        st.info("💡 Suggestion: Water quality is good, but regular testing is recommended.")
    else:
        st.error("❌ Water is NOT SAFE to drink")
        st.warning("⚠️ Suggestion: Boil or filter water before drinking.")

# Footer
st.markdown("---")
st.write("📊 Model used: Machine Learning (Classification)")