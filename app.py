import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load your model
model = joblib.load('model.pkl')

# Encoding dictionaries for categorical features
gender_encoding = {"Male": 1, "Female": 0}
education_level_encoding = {'Uneducated': 0, 'High School': 1, 'College': 2, 'Graduate': 3, 'Post-Graduate': 4, 'Doctorate': 5}
marital_status_encoding = {"Single": 0, "Married": 1, "Divorced": 2}
income_category_encoding = {"Less than $40K": 0, "$40K - $60K": 1, "$60K - $80K": 2, "$80K - $120K": 3, "$120K +": 4}
card_category_encoding = {"Blue": 0, "Silver": 1, "Gold": 2, "Platinum": 3}

# Function to predict churn
def predict_churn(input_data):
    input_df = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(input_df)
    return prediction[0]

# Custom CSS for changing background, text color, and resetting small button text
st.markdown("""
    <style>
    /* Application background */
    .main {
        background-color: white; /* Set background color to white */
    }
    
    /* Text color for headers and labels */
    h1, h2, h3, h4, h5, h6, label,p {
        color: darkblue !important; /* Set text color to dark blue */
    }
    

    /* Button styling */
    .stButton>button {
        background-color: orange; /* Set button background color */
        color: white; /* Reset button text color to white */
        font-size: 16px; /* Adjust font size */
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: darkblue; /* Change background on hover */
        color: white; /* Keep button text white on hover */
    }
    </style>
""", unsafe_allow_html=True)



st.title("Customer Attrition Prediction")

# Input features
st.subheader("Enter Customer Information")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", options=list(gender_encoding.keys()))
dependent_count = st.number_input("Dependent Count", min_value=0, value=0)
education_level = st.selectbox("Education Level", options=list(education_level_encoding.keys()))
marital_status = st.selectbox("Marital Status", options=list(marital_status_encoding.keys()))
income_category = st.selectbox("Income Category", options=list(income_category_encoding.keys()))
card_category = st.selectbox("Card Category", options=list(card_category_encoding.keys()))

# Additional numerical inputs
months_on_book = st.number_input("Months on Book", min_value=0, value=0)
total_relationship_count = st.number_input("Total Relationship Count", min_value=0, value=0)
months_inactive_12_mon = st.number_input("Months Inactive (last 12 months)", min_value=0, value=0)
contacts_count_12_mon = st.number_input("Contacts Count (last 12 months)", min_value=0, value=0)
credit_limit = st.number_input("Credit Limit", min_value=0.0, value=0.0)
total_revolving_bal = st.number_input("Total Revolving Balance", min_value=0.0, value=0.0)
avg_open_to_buy = st.number_input("Average Open to Buy", min_value=0.0, value=0.0)
total_amt_chng_q4_q1 = st.number_input("Total Amount Change Q4-Q1", min_value=0.0, value=0.0)
total_trans_amt = st.number_input("Total Transaction Amount", min_value=0.0, value=0.0)
total_trans_ct = st.number_input("Total Transaction Count", min_value=0, value=0)
total_ct_chng_q4_q1 = st.number_input("Total Count Change Q4-Q1", min_value=0.0, value=0.0)
avg_utilization_ratio = st.number_input("Average Utilization Ratio", min_value=0.0, value=0.0)

# Prepare input data for prediction using encodings
input_data = {
    'Age': age,
    'Gender': gender_encoding[gender],
    'Dependent_count': dependent_count,
    'Education_Level': education_level_encoding[education_level],
    'Marital_Status': marital_status_encoding[marital_status],
    'Income_Category': income_category_encoding[income_category],
    'Card_Category': card_category_encoding[card_category],
    'Months_on_book': months_on_book,
    'Total_Relationship_Count': total_relationship_count,
    'Months_Inactive_12_mon': months_inactive_12_mon,
    'Contacts_Count_12_mon': contacts_count_12_mon,
    'Credit_Limit': credit_limit,
    'Total_Revolving_Bal': total_revolving_bal,
    'Avg_Open_To_Buy': avg_open_to_buy,
    'Total_Amt_Chng_Q4_Q1': total_amt_chng_q4_q1,
    'Total_Trans_Amt': total_trans_amt,
    'Total_Trans_Ct': total_trans_ct,
    'Total_Ct_Chng_Q4_Q1': total_ct_chng_q4_q1,
    'Avg_Utilization_Ratio': avg_utilization_ratio
}

# Make prediction
if st.button("Predict"):
    prediction = predict_churn(input_data)
    st.write(f"Churn Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
