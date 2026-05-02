#  Insurance Claim Risk Prediction System

##  Project Overview

This project is a machine learning-based system designed to predict whether a customer is likely to file an insurance claim. It simulates a real-world insurance risk assessment tool used by companies such as CIC Insurance.

The system analyzes customer demographics, driving behavior, and historical claim patterns to estimate risk and provide business recommendations.

---

##  Objectives

* Predict insurance claim likelihood (classification)
* Identify high-risk customers early
* Support decision-making for premium pricing and underwriting

---

##  Dataset

A synthetic dataset was used, containing:

* Customer demographics (age, gender, income)
* Driving behavior (experience, previous claims)
* Insurance data (premium amount)
* Target variable: `claim_status`

---

##  Feature Engineering

Key engineered features include:

* `risk_flag_young` – identifies young drivers
* `risk_flag_new_driver` – flags inexperienced drivers
* `claim_ratio` – previous claims relative to age
* `income_premium_ratio` – affordability indicator

---

##  Machine Learning Models

* Logistic Regression (baseline)
* Random Forest (final model)
* Hyperparameter tuning using GridSearchCV

---

## Model Performance

* Accuracy: High (varies depending on run)
* Optimized using F1-score to balance risk prediction
* Evaluated using confusion matrix and classification report

---

##  Streamlit Application

An interactive web app was built using Streamlit to:

* Input customer details
* Predict claim risk
* Display probability and risk category
* Provide business recommendations

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---

##  How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Yobe47/insurance-claim-prediction.git
cd insurance-claim-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
cd app
streamlit run streamlit_app.py
```

---

## Business Value

This system can help insurance companies:

* Reduce financial losses
* Improve customer risk profiling
* Optimize premium pricing strategies

---

---

## 👨‍💻 Author

Andrew Banda

---

## 📌 Future Improvements

* Add SHAP explainability for model transparency
* Deploy application online
* Integrate real-world insurance datasets
