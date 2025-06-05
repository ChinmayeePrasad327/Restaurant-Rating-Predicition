import streamlit as st
import pandas as pd
import pickle
import datetime
import os

# Load model and encoders
with open('best_model_rf.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍽️", layout="centered")

st.title("🍽️ Restaurant Rating Prediction App")
st.markdown("Use this form to enter restaurant details and predict its **aggregate rating**.")

# --- FORM LAYOUT ---
with st.form("rating_form"):
    cuisine = st.selectbox("Cuisines*", ["Select"] + ["Pizza", "North Indian", "South Indian", "Chinese", "Continental"])
    cost = st.number_input("Average Cost for Two*", min_value=0, step=50, format="%d")
    price_range = st.selectbox("Price Range (1-4)*", ["Select"] + [1, 2, 3, 4])
    votes = st.number_input("Votes*", min_value=0, step=10, format="%d")
    table_booking = st.radio("Has Table Booking?*", [ "Yes", "No"])
    online_delivery = st.radio("Has Online Delivery?*", ["Yes", "No"])
    delivering_now = st.radio("Is Delivering Now?*", ["Yes", "No"])
    country = st.selectbox("Country*", ["Select"] + ["India", "UAE", "United States", "Brazil"])

    submitted = st.form_submit_button("Predict")

# --- ON PREDICT ---
if submitted:
    if "Select" in [cuisine, price_range, table_booking, online_delivery, delivering_now, country]:
        st.error("Please fill all required fields marked with *.")
        st.stop()

    input_data = {
        'Cuisines': cuisine,
        'Average Cost for two': cost,
        'Price range': price_range,
        'Votes': votes,
        'Has Table booking': table_booking,
        'Has Online delivery': online_delivery,
        'Is delivering now': delivering_now,
        'Country': country
    }

    df = pd.DataFrame([input_data])

    # Apply label encoding
    for col in df.columns:
        if col in label_encoders:
            le = label_encoders[col]
            if df[col][0] in le.classes_:
                df[col] = le.transform(df[col])
            else:
                st.error(f"Unknown input '{df[col][0]}' in column: '{col}'")
                st.stop()

    # Align columns
    if hasattr(model, 'feature_names_in_'):
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0
        df = df[model.feature_names_in_]

    # Predict (no scaling needed)
    prediction = round(model.predict(df)[0], 2)

    # --- Color-coded rating meaning ---
    if prediction >= 4:
        label = "💚 Excellent"
    elif prediction >= 3:
        label = "💛 Good"
    elif prediction >= 2:
        label = "🧡 Average"
    else:
        label = "❤️ Poor"

    st.success(f"⭐ Predicted Aggregate Rating: **{prediction}**")
    st.info(f"Interpretation: {label}")

    # --- Log prediction ---
    log_data = df.copy()
    log_data['Predicted Rating'] = prediction
    log_data['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_file = "predictions_log.csv"
    if os.path.exists(log_file):
        prev_logs = pd.read_csv(log_file)
        new_logs = pd.concat([prev_logs, log_data], ignore_index=True)
    else:
        new_logs = log_data

    new_logs.to_csv(log_file, index=False)
    st.toast("📁 Prediction logged successfully!")
