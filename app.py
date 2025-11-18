import streamlit as st
import pandas as pd 
import joblib

# Define the features that were actually encoded in your core script
# Excludes 'Job' (input as integer) and 'Risk' (target variable)
CATEGORICAL_FEATURES = ["Sex", "Housing", "Saving accounts", "Checking account", "Purpose"] 

# --- Load Model and Encoders ---
try:
    # Load the final trained model (matching the name saved in the core script)
    model = joblib.load("final_credit_risk_model.pkl")
    
    # Load the feature encoders safely
    encoders = {}
    for col in CATEGORICAL_FEATURES:
        encoders[col] = joblib.load(f"{col}_label_encoder.pkl") 

except FileNotFoundError as e:
    st.error(f"Required file not found: {e.filename}. Please ensure you ran your core modeling script successfully and all encoder files are present.")
    st.stop()
except Exception as e:
    # Catch any potential error during loading (e.g., corrupted file)
    st.error(f"An unexpected error occurred during file loading. Is the model name correct? Error: {e}")
    st.stop()
# ------------------------------

st.title("Credit Risk Prediction App 🏦")
st.markdown("Enter the applicant's details to assess the likelihood of 'Bad Credit Risk' (0) vs. 'Good Credit Risk' (1).")

# --- Input Fields ---
age = st.number_input("Age", min_value=18, max_value=100, value=30)
# Job is input as the encoded integer value (0, 1, 2, 3)
job = st.selectbox("Job (0: Unemployed/Non-res, 1: Unskilled/Res, 2: Skilled, 3: Highly Skilled)", [0, 1, 2, 3])
credit_amount = st.number_input("Credit Amount", min_value=100, max_value=100000, value=1000)
duration = st.number_input("Duration (in months)", min_value=1, max_value=72, value=12)

# Sex (Corrected: only includes categories known to the encoder)
sex = st.selectbox("Sex", ["male", "female"]) 

housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "quite rich", "rich", "no known savings"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich", "no known checking account"])

# Purpose (Using the categories present in the German Credit Data)
purpose = st.selectbox("Purpose", [
    "car", "furniture/equipment", "radio/television", "domestic appliances", 
    "repairs", "education", "vacation/others", "retraining", "business"
])


# --- Prediction Logic ---
if st.button("Predict Credit Risk"):
    try:
        # Prepare input for prediction by transforming categorical strings to integers
        input_data = {
            "Age": [age],
            "Job": [job], # Job is already the expected integer
            "Credit amount": [credit_amount],
            "Duration": [duration],
            
            # Apply transformation using the loaded encoders for string inputs
            "Sex": [encoders["Sex"].transform([sex])[0]],
            "Housing": [encoders["Housing"].transform([housing])[0]],
            "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
            "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
            "Purpose": [encoders["Purpose"].transform([purpose])[0]]
        }
        
        input_df = pd.DataFrame(input_data)

        # Predict
        prediction = model.predict(input_df)
        
        # Risk decoding: 0 = Bad Risk, 1 = Good Risk
        risk = "Good Credit Risk" if prediction[0] == 1 else "Bad Credit Risk"
        st.success(f"The predicted credit risk is: **{risk}**")

    except ValueError as e:
        # This catches errors if an input category (like a new 'Purpose') doesn't match the encoder
        st.error(f"Input category mismatch: A selected category is not recognized by the model's encoder. Detail: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred during prediction: {e}")