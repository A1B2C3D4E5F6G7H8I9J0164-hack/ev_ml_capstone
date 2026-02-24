⚡ EV RANGE PREDICTION SYSTEM
🚗 Machine Learning Based Electric Vehicle Analytics Platform

An end-to-end Machine Learning web application that predicts the driving range of electric vehicles (EVs) using vehicle specifications.
The system is trained using classical ML models and deployed as a public, interactive web application.

🚀 WHAT DOES THIS PROJECT DO?

🔮 Predicts EV driving range using ML

📂 Supports CSV upload for batch predictions

🧠 Allows manual input for instant results

🌐 Fully deployed and publicly accessible

🎨 Modern and clean UI built with Streamlit

🎯 PROBLEM STATEMENT

Electric vehicles have varying driving ranges depending on their specifications such as efficiency, acceleration, and performance parameters.

❓ Why is this important?

Helps understand EV performance characteristics

Supports EV analytics and planning

Enables data-driven decision-making

This project addresses the problem using supervised machine learning (regression).

🧠 SYSTEM WORKFLOW
1️⃣ DATA PREPROCESSING

Removed non-informative columns (Brand, Model)

Handled missing values

Converted categorical variables using one-hot encoding

Ensured a clean, numerical feature space

2️⃣ FEATURE ENGINEERING

Key input features used:

💰 Price (€)

⚙️ Energy Efficiency (Wh/km)

🚀 Acceleration (0–100 km/h)

🏎 Top Speed (km/h)

📊 Encoded categorical attributes

3️⃣ MODEL TRAINING

The following regression models were implemented and compared:

🌲 Random Forest Regressor

📈 Gradient Boosting Regressor

The final model was selected based on performance metrics.

4️⃣ MODEL EVALUATION

The models were evaluated using standard regression metrics:

MAE – Mean Absolute Error

RMSE – Root Mean Squared Error

R² Score – Coefficient of Determination

These metrics ensure both accuracy and robustness.

🖥️ APPLICATION FEATURES
✨ INTERACTIVE WEB INTERFACE

📂 Batch Prediction using CSV upload

🧠 Manual Prediction using form inputs

📊 Real-time prediction results

⬇️ Downloadable output files

🎨 Modern UI with clean visual hierarchy

🛠 TECHNOLOGY STACK
🔧 TOOLS & FRAMEWORKS USED

Programming Language: Python

Machine Learning: scikit-learn

Data Processing: pandas, numpy

Model Serialization: joblib

UI Framework: Streamlit

Deployment Platform: Streamlit Community Cloud

🌍 LIVE DEPLOYMENT
✅ Publicly Hosted Application

The application is deployed online and accessible through a public link.

🔗 Live App Link:
PASTE YOUR STREAMLIT LINK HERE

📁 PROJECT STRUCTURE
ev_ml_capstone/
│
├── app.py                # Streamlit application
├── ev_model_safe.pkl     # Trained ML model
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
▶️ HOW TO RUN LOCALLY
pip install -r requirements.txt
streamlit run app.py
🔒 DEPLOYMENT STABILITY DESIGN

To ensure reliability across different environments:

Preprocessing is decoupled from the trained model

Input features are dynamically aligned during inference

Prevents Python and scikit-learn version incompatibility issues

📌 KEY TAKEAWAYS

✅ Built a complete ML pipeline

✅ Compared multiple regression models

✅ Designed a modern, user-friendly UI

✅ Successfully deployed a real ML application

🔮 FUTURE SCOPE

Agent-based EV infrastructure planning

Charging demand prediction

Optimization-driven EV analytics (Milestone 2)
