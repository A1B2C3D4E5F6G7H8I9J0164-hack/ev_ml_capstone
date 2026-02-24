# ⚡ EV Range Prediction System  
### 🚗 Machine Learning–Powered Electric Vehicle Analytics Platform

An **end-to-end Machine Learning web application** that predicts the **driving range of electric vehicles (EVs)** using key vehicle specifications.  
Built with classical ML models and deployed as a **public, interactive Streamlit web app**.

---

## 🚀 What Does This Project Do?

🔮 Predicts EV driving range using supervised ML (regression)  
📂 Supports CSV upload for batch predictions  
🧠 Allows manual input for instant results  
🌐 Fully deployed and publicly accessible  
🎨 Modern and clean UI built with Streamlit  

---

## 🎯 Problem Statement

Electric vehicles exhibit **significant variation in driving range** depending on factors such as efficiency, acceleration, and performance characteristics.

### ❓ Why is this important?

- Helps analyze and compare EV performance  
- Supports EV analytics and planning  
- Enables data-driven decision-making  

This project addresses the problem using **supervised machine learning regression models**.

---

## 🧠 System Workflow

### 1️⃣ Data Preprocessing
- Removed non-informative columns (Brand, Model)
- Handled missing values
- Converted categorical variables using **One-Hot Encoding**
- Ensured a clean, numerical feature space

---

### 2️⃣ Feature Engineering

Key input features:

- 💰 Price (€)
- ⚙️ Energy Efficiency (Wh/km)
- 🚀 Acceleration (0–100 km/h)
- 🏎 Top Speed (km/h)
- 📊 Encoded categorical attributes

---

### 3️⃣ Model Training

Regression models implemented and compared:

- 🌲 Random Forest Regressor  
- 📈 Gradient Boosting Regressor  

The final model was selected based on evaluation performance.

---

### 4️⃣ Model Evaluation

Evaluation metrics used:

- **MAE** – Mean Absolute Error  
- **RMSE** – Root Mean Squared Error  
- **R² Score** – Coefficient of Determination  

These metrics ensure both accuracy and robustness.

---

## 🖥️ Application Features

✨ Interactive web interface  
📂 Batch prediction using CSV upload  
🧠 Manual prediction using form inputs  
📊 Real-time prediction results  
⬇️ Downloadable output files  
🎨 Clean UI with modern visual hierarchy  

---

## 🛠 Technology Stack

### 🔧 Tools & Frameworks

- **Programming Language:** Python  
- **Machine Learning:** scikit-learn  
- **Data Processing:** pandas, numpy  
- **Model Serialization:** joblib  
- **UI Framework:** Streamlit  
- **Deployment:** Streamlit Community Cloud  

---

## 🌍 Live Deployment

✅ Publicly Hosted Application

🔗 **Live App Link:**  
👉 PASTE YOUR STREAMLIT LINK HERE

---

## 📁 Project Structure

```bash
ev_ml_capstone/
│
├── app.py                # Streamlit application
├── ev_model_safe.pkl     # Trained ML model
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔒 Deployment Stability Design

To ensure reliability across environments:

- Preprocessing is decoupled from the trained model  
- Input features are dynamically aligned during inference  
- Prevents Python and scikit-learn version incompatibility issues  

---

## 📌 Key Takeaways

✅ Built a complete ML pipeline  
✅ Compared multiple regression models  
✅ Designed a modern, user-friendly UI  
✅ Successfully deployed a real ML application  

---

## 🔮 Future Scope

- 🤖 Agent-based EV infrastructure planning  
- 🔌 Charging demand prediction  
- 📈 Optimization-driven EV analytics (Milestone 2)
