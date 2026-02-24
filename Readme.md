⚡ EV Range Prediction System

An end-to-end Machine Learning application that predicts electric vehicle driving range using vehicle specifications.
Built, deployed, and accessible as a live web application.

🚀 What This Project Does

Predicts EV driving range using ML

Accepts CSV uploads for batch predictions

Allows manual input for instant predictions

Deployed publicly with a modern web interface

🎯 Problem Statement

Electric vehicles vary significantly in driving range based on their specifications.
Accurately predicting range helps in:

Understanding EV performance

Supporting data-driven EV adoption

Improving analytics for EV planning

This project solves the problem using supervised machine learning regression.

🧠 How It Works
1️⃣ Data Preprocessing

Removed non-informative columns (Brand, Model)

Cleaned missing values

Converted categorical features using one-hot encoding

Prepared numerical feature space for ML models

2️⃣ Feature Engineering

Important features include:

💰 Price (€)

⚙️ Efficiency (Wh/km)

🚀 Acceleration (0–100 km/h)

🏎 Top Speed (km/h)

Encoded categorical attributes

3️⃣ Model Training

Two regression models were trained and compared:

🌲 Random Forest Regressor

📈 Gradient Boosting Regressor

The best-performing model was selected based on evaluation metrics.

4️⃣ Model Evaluation

Models were evaluated using:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

🖥️ Application Features

✨ Modern UI built with Streamlit

📂 Upload CSV for bulk predictions

🧠 Manual input for single EV prediction

📊 Instant results display

⬇️ Downloadable prediction output

🌐 Live hosted application

🛠 Tech Stack
Layer	Tools
Language	Python
ML	scikit-learn
Data	pandas, numpy
Model Storage	joblib
UI	Streamlit
Hosting	Streamlit Community Cloud
🌍 Live Deployment

The application is publicly hosted and accessible online.

🔗 Live App:
PASTE YOUR STREAMLIT LINK HERE

📁 Project Structure
ev_ml_capstone/
│
├── app.py                # Streamlit application
├── ev_model_safe.pkl     # Trained ML model
├── requirements.txt      # Dependencies
├── README.md             # Documentation
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
🔒 Deployment Stability

To ensure reliable deployment across environments:

Preprocessing is handled outside the model

Input features are dynamically aligned during inference

This avoids serialization and version compatibility issues

📌 Key Takeaways

Built a complete ML pipeline from scratch

Compared multiple regression models

Designed and deployed a real web application

Focused on stability, usability, and clarity

🧠 What’s Next

Agent-based EV infrastructure planning (Milestone 2)

Demand-based charging analytics

Optimization-driven decision support
