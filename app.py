import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="EV Range Predictor",
    page_icon="⚡",
    layout="wide"
)

# -------------------------------
# Custom CSS (Modern UI)
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3, h4 {
    color: #ffffff;
}
p, label, div {
    color: #d1d5db;
}
.card {
    background: #161b22;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 0 0 1px #30363d;
}
.metric-box {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 1.2rem;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 1.2rem;
}
hr {
    border: 1px solid #30363d;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Model
# -------------------------------
bundle = joblib.load("ev_model_safe.pkl")
model = bundle["model"]
model_columns = bundle["columns"]

# -------------------------------
# Header Section
# -------------------------------
st.markdown("""
<div class="card">
    <h1>⚡ EV Range Prediction System</h1>
    <p>
        AI-powered system to estimate <b>electric vehicle driving range</b> 
        using vehicle specifications. Built with Machine Learning & deployed live.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------------------
# CSV Upload Section
# -------------------------------
st.markdown("""
<div class="card">
    <h2>📂 Batch Prediction</h2>
    <p>Upload a CSV file containing EV specifications to predict driving range.</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload EV Dataset (CSV)",
    type=["csv"],
    label_visibility="collapsed"
)

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data.head(), use_container_width=True)

    data_encoded = pd.get_dummies(data)
    data_encoded = data_encoded.reindex(columns=model_columns, fill_value=0)

    predictions = model.predict(data_encoded)
    data["Predicted_Range_Km"] = predictions

    st.subheader("Prediction Results")
    st.dataframe(data.head(), use_container_width=True)

    st.download_button(
        "⬇️ Download Predictions",
        data=data.to_csv(index=False),
        file_name="ev_predictions.csv",
        mime="text/csv"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------
# Manual Prediction Section
# -------------------------------
st.markdown("""
<div class="card">
    <h2>🧠 Manual Prediction</h2>
    <p>Enter vehicle specifications to instantly estimate driving range.</p>
</div>
""", unsafe_allow_html=True)

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        price = st.number_input("💰 Price (€)", min_value=0)
        efficiency = st.number_input("⚙️ Efficiency (Wh/km)", min_value=0)

    with col2:
        acceleration = st.number_input("🚀 Acceleration 0–100 (sec)", min_value=0.0)
        top_speed = st.number_input("🏎 Top Speed (km/h)", min_value=0)

    submitted = st.form_submit_button("🔮 Predict Range")

if submitted:
    input_df = pd.DataFrame([{
        "PriceEuro": price,
        "Efficiency_WhKm": efficiency,
        "AccelSec": acceleration,
        "TopSpeed_KmH": top_speed
    }])

    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_encoded)[0]

    st.markdown(f"""
    <div class="metric-box">
        🚗 Estimated Driving Range<br><br>
        <b>{prediction:.2f} km</b>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Footer
# -------------------------------
st.write("")
st.markdown("""
<p style="text-align:center; font-size:14px; color:#9ca3af;">
Built with ❤️ using Machine Learning & Streamlit
</p>
""", unsafe_allow_html=True)