import streamlit as st
import numpy as np
import joblib

# =========================
# 1. LOAD MODEL ONLY
# =========================
model = joblib.load("models/best_insurance_model.pkl")

# =========================
# 2. PAGE CONFIG
# =========================
st.set_page_config(page_title="Insurance Risk Predictor", layout="centered")

st.title(" Insurance Claim Risk Predictor")
st.write("Predict whether a customer is likely to file an insurance claim.")

# =========================
# 3. USER INPUTS
# =========================
st.subheader("Enter Customer Details")

age = st.slider("Age", 18, 80, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
annual_income = st.number_input("Annual Income", 1000, 500000, 50000)
vehicle_type = st.selectbox("Vehicle Type", ["Car", "Bike"])
driving_experience = st.slider("Driving Experience (years)", 0, 40, 5)
previous_claims = st.slider("Previous Claims", 0, 5, 0)
premium_amount = st.number_input("Premium Amount", 100, 100000, 5000)

# =========================
# 4. MANUAL ENCODING (FIXED)
# =========================
gender_encoded = 1 if gender == "Male" else 0
vehicle_encoded = 1 if vehicle_type == "Car" else 0

# =========================
# 5. FEATURE ENGINEERING
# =========================
risk_flag_young = 1 if age < 25 else 0
risk_flag_new_driver = 1 if driving_experience < 3 else 0
claim_ratio = previous_claims / (age + 1)
income_premium_ratio = annual_income / (premium_amount + 1)

# =========================
# 6. PREDICTION
# =========================
if st.button("🔍 Predict Risk"):

    input_data = np.array([[
        age,
        gender_encoded,
        annual_income,
        vehicle_encoded,
        driving_experience,
        previous_claims,
        premium_amount,
        risk_flag_young,
        risk_flag_new_driver,
        claim_ratio,
        income_premium_ratio
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # =========================
    # 7. RESULTS
    # =========================
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(" High Risk: Likely to file a claim")
    else:
        st.success(" Low Risk: Unlikely to file a claim")

    st.write(f"Probability of Claim: {probability:.2f}")

    # Risk category
    if probability > 0.7:
        st.warning(" Very High Risk")
    elif probability > 0.4:
        st.info(" Medium Risk")
    else:
        st.success("Low Risk")

    # =========================
    # 8. BUSINESS RECOMMENDATION
    # =========================
    st.markdown("###  Recommendation")

    if probability > 0.7:
        st.write("Increase premium or flag for manual review.")
    elif probability > 0.4:
        st.write("Monitor customer risk and adjust pricing carefully.")
    else:
        st.write("Customer is low risk. Standard premium applies.")