# Import the neccessary Libraries for this Project.
import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib as jb 

# Set App configuration.
st.set_page_config(page_title="Tel-communication", layout="wide", initial_sidebar_state= "auto", page_icon=r"C:\Users\Neptune\Downloads\chat.png")

# Head title
st.markdown("-" * 50)
st.title("Welcome to Tel-communication Prediction")
st.markdown("This Project enable user to select various factors that can infulence the decision of a customer to churn or not to.")
st.subheader("Kindly click the icon on your left to start now!!.")
st.image(r"C:\Users\Neptune\Downloads\Gente.jfif", width= 250 )
st.markdown("-" * 50)

# To Deploy the model into the app.
@st.cache_resource # To load the model once 
def  load_model():
    try:
        modelpath = jb.load("RfC.pki")
        return modelpath
    except Exception as e:
        st.error(f"The error message: {e}")
        return None
        
Model = load_model()

# Factors to enable the Model to make Prediction.
with st.sidebar:
    st.header("Factors to determine If You will leave or not.")
    Tenure_Months = st.slider("Tenure Months", min_value = 0, max_value= 72, value = 0)
    Total_Charges = st.sidebar.number_input("Total Charges", min_value= 100, max_value= 12000, value = 100, step = 20)
    Monthly_Charges = st.slider("Monthly Charges", min_value= 18.25, max_value= 118.75, value = 18.25, step = 2.10)
    Contract = st.selectbox("Contract", ['Month-to-month', 'Two year', 'One year'])
    Tech_Support = st.selectbox("Tech Support", ['No', 'Yes'])
    Payment_Method = st.selectbox("Payment Method", ['Mailed check', 'Electronic check', 'Bank transfer (automatic)','Credit card (automatic)'])
    Online_Security = st.selectbox("Online Security", ['No', 'Yes'])
    Senior_Citizen = st.selectbox("Senior Citizen", ['No', 'Yes'])
    Dependents = st.selectbox('Dependents', ['No', 'Yes'])

# To convert the Categorical values in Numerical values by Map the selection with a number. 
sel= {'Month-to-month': 0, 'Two year': 1, 'One year': 3}
sel1 = {'No': 0, 'Yes': 1}
sel2 = {'Mailed check': 0, 'Electronic check': 1, 'Bank transfer (automatic)': 2,'Credit card (automatic)': 3}
sel3 = {'No': 0, 'Yes': 1}
sel4 = {'No': 0, 'Yes': 1}
sel5 = {'No': 0, 'Yes': 1}

cat_col = sel[Contract]
cat_col1 = sel1[Tech_Support]
cat_col2 = sel2[Payment_Method]
cat_col3 = sel3[Online_Security]
cat_col4 = sel4[Senior_Citizen]
cat_col5 = sel5[Dependents]


# The Independent Variables to Fit.
features = np.array([[Tenure_Months, cat_col, Total_Charges, Monthly_Charges, cat_col1, cat_col2, cat_col3, cat_col4, cat_col5]])

Predict = st.sidebar.button("Predict", width = "stretch", type ="primary")
if Predict:
    try:
        outcome = Model.predict(features)[0]
        if outcome == 1:
            st.markdown("⚠️ HIGH RISK OF CHURN")
            st.error("This customer is likely to leave the service.")
        else: # NOT CHURN
            st.markdown('✅ LOW RISK / LOYAL')
            st.success("This customer is likely to stay.")
    except Exception as e:
        st.error(f"The Error Message: {e}")
