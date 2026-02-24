EV RANGE PREDICTION SYSTEM

An AI-powered machine learning application to predict the driving range of electric vehicles (EVs) using vehicle specifications. This project demonstrates an end-to-end ML workflow including data preprocessing, feature engineering, model training, evaluation, UI development, and cloud deployment.

PROJECT OBJECTIVE

The objective of this project is to build a machine learning–based system that estimates the driving range of an electric vehicle based on its technical specifications such as efficiency, acceleration, price, and top speed.

This project aligns with intelligent EV analytics and supports data-driven decision-making for electric mobility and infrastructure planning.

APPROACH AND METHODOLOGY

Data Preprocessing

Removed irrelevant columns such as brand and model

Handled missing values

Converted categorical variables using one-hot encoding

Ensured all features were numerical and clean

Feature Engineering
Key features used for prediction include:

Vehicle price

Energy efficiency (Wh/km)

Acceleration (0–100 km/h)

Top speed

Encoded categorical attributes

Model Training
The following regression models were trained and compared:

Random Forest Regressor

Gradient Boosting Regressor

The best-performing model was selected based on evaluation metrics.

Model Evaluation
Models were evaluated using:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

APPLICATION FEATURES

Batch prediction by uploading CSV files

Manual prediction using vehicle specifications

Interactive and modern user interface built with Streamlit

Downloadable prediction results

Publicly hosted web application

TECHNOLOGY STACK

Programming Language: Python

Machine Learning: scikit-learn

Data Processing: pandas, numpy

Model Serialization: joblib

UI Framework: Streamlit

Deployment Platform: Streamlit Community Cloud

DEPLOYMENT

The application is publicly deployed using Streamlit Community Cloud, satisfying the mandatory hosting requirement.

Live Application Link:
PASTE YOUR STREAMLIT LINK HERE

PROJECT STRUCTURE

ev_ml_capstone
|-- app.py
|-- ev_model_safe.pkl
|-- requirements.txt
|-- README.md

HOW TO RUN LOCALLY

pip install -r requirements.txt
streamlit run app.py

DEPLOYMENT STABILITY NOTE

To ensure deployment stability across different Python and scikit-learn versions, preprocessing was decoupled from the trained model. Input data is aligned dynamically during inference to prevent compatibility issues.

CONCLUSION

This project demonstrates a complete machine learning pipeline from raw data processing to a deployed web application. It highlights practical skills in model building, evaluation, deployment, and user interface development.
