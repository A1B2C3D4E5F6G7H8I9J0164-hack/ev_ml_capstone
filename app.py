import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("ev_range_prediction_model.pkl")

st.set_page_config(page_title="EV Range Predictor", layout="wide")

st.title("⚡ EV Range Prediction System")
st.write("Predict EV driving range using vehicle specifications.")


st.header("📂 Upload CSV for Batch Prediction")

uploaded_file = st.file_uploader("Upload EV dataset", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(data.head())

    predictions = model.predict(data)
    data["Predicted_Range_Km"] = predictions

    st.subheader("Predictions")
    st.dataframe(data.head())

    st.download_button(
        label="Download Predictions CSV",
        data=data.to_csv(index=False),
        file_name="ev_predictions.csv",
        mime="text/csv"
    )

st.markdown("---")


st.header("🧠 Manual Prediction")

with st.form("prediction_form"):
    price = st.number_input("Price (€)", min_value=0)
    efficiency = st.number_input("Efficiency (Wh/km)", min_value=0)
    acceleration = st.number_input("Acceleration 0-100 (sec)", min_value=0.0)
    top_speed = st.number_input("Top Speed (km/h)", min_value=0)

    submitted = st.form_submit_button("Predict Range")

if submitted:
    input_df = pd.DataFrame([{
        "PriceEuro": price,
        "Efficiency_WhKm": efficiency,
        "AccelSec": acceleration,
        "TopSpeed_KmH": top_speed
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"🚗 Estimated Driving Range: {prediction:.2f} km")