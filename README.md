# 🍽️ Restaurant Rating Prediction App

This project is a **Machine Learning-based Web App** that predicts a restaurant’s aggregate rating based on key features like cuisine, cost, delivery options, and more.

Built as part of my internship task with a focus on data preprocessing, feature encoding, model building, and UI integration using **Streamlit**.

---

## 🔍 Problem Statement

Restaurants receive reviews and votes from users, but can we predict their **aggregate rating** just from operational features? This app answers that by analyzing key attributes to generate a predicted rating.

---

## 🧠 Tech Stack & Concepts Used

- **Python**
- **Pandas & NumPy** for data manipulation
- **LabelEncoder** for categorical encoding
- **Random Forest Regressor** for prediction (no scaling required)
- **Streamlit** for building the user-friendly interface
- **Pickle** for model serialization
- **CSV Logging** for saving user predictions
- **Design Thinking** — clean, form-based layout with color-coded outputs

---

## 📊 Input Features

- Cuisines  
- Average Cost for Two  
- Price Range (1 to 4)  
- Votes  
- Table Booking (Yes/No)  
- Online Delivery (Yes/No)  
- Delivering Now (Yes/No)  
- Country  

---

## 🎯 Output

- ⭐ Predicted **Aggregate Rating**
- 🎨 Color-coded interpretation (Excellent, Good, Average, Poor)

---

## 📁 Files Included

- `best_model_rf.pkl` – Trained Random Forest model  
- `label_encoders.pkl` – Label encoders for categorical inputs  
- `streamlit_app.py` – Final app code  
- `Cognifyz_Restaurant_Rating_Prediction.ipynb` – Full notebook with preprocessing and model training  
- `predictions_log.csv` – Appends each user prediction with timestamp

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
