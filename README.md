# 🍽️ Restaurant Rating Prediction App

This project is a **Machine Learning-based Web App** that predicts a restaurant’s aggregate rating based on key features like cuisine, cost, delivery options, and more.

Built as part of my internship task with a focus on data preprocessing, feature encoding, experimenting with multiple regression models, and deploying a user-friendly UI using **Streamlit**.

---

## 🔍 Problem Statement

Restaurants receive reviews and votes from users, but can we predict their **aggregate rating** solely from operational features? This app answers that by analyzing key attributes to generate an accurate predicted rating.

---

## 🧠 Tech Stack & Concepts Used

- **Python**  
- **Pandas & NumPy** for data manipulation  
- **LabelEncoder** for categorical variable encoding  
- **Regression Models Tried:**  
  - Linear Regression  
  - Decision Tree Regressor  
  - Random Forest Regressor (selected as best performer)  
- **Model Evaluation Metrics:** Mean Squared Error (MSE), R-squared (R²)  
- **Streamlit** for building an interactive and clean user interface  
- **Pickle** for saving and loading the trained model and encoders  
- **CSV Logging** for recording user inputs and predictions  

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
- 🎨 Color-coded interpretation (Excellent, Good, Average, Poor) for intuitive feedback  

---

## 🧩 Model Selection & Performance

I trained and compared three regression models:

| Model               | Mean Squared Error (MSE) | R² Score  | Notes                       |
|---------------------|--------------------------|-----------|-----------------------------|
| Linear Regression   | Higher                   | Lower     | Underfit the dataset         |
| Decision Tree       | Moderate                 | Moderate  | Overfitting on training data |
| **Random Forest**   | **Lowest**               | **Highest** | Best generalization & accuracy |

Hence, **Random Forest Regressor** was chosen as the final model for prediction due to its superior performance and robustness.

---

## 📁 Files Included

- `best_model_rf.pkl` – Trained Random Forest model  
- `label_encoders.pkl` – Label encoders for categorical inputs  
- `streamlit_app.py` – Interactive Streamlit app code  
- `Cognifyz_Restaurant_Rating_Prediction.ipynb` – Complete notebook with data preprocessing, exploratory analysis, model training, and evaluation  
- `predictions_log.csv` – CSV file logging all user inputs and predicted ratings with timestamps  

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
