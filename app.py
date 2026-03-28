import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("💧 Water Quality Analyzer")

st.write("Enter water parameters:")

ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
solids = st.number_input("TDS", 0.0, 50000.0, 10000.0)
chloramines = st.number_input("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0, 250.0)
conductivity = st.number_input("Conductivity", 0.0, 1000.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 10.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 200.0, 80.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

if st.button("Check Water Quality"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon,
                            trihalomethanes, turbidity]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Water is SAFE to drink")
    else:
        st.error("❌ Water is NOT SAFE to drink")