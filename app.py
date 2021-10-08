"""Main App logic for prediction."""
import streamlit as st
import numpy as np
import pandas as pd
from joblib import load


# Load Model 
model = load('model_health')

def convert(val):
    if val == 'Yes': val = 1
    else: val = 0
    return val

def change(val):
    if val == 0:
        return 1
    else:
        return 0

# Main function that holds logic
def run():

    res = []

    # Display Bean Icon and title
    st.title('Diabetes Prediction App')
    st.image('image.jpg', use_column_width=True)
    st.subheader("Fill in the questions and click on the button below.")

    age = st.number_input('How old are you ?', min_value=0, step=1)
    res.append(age)
    
    gender = st.radio("What is your Gender?",("Male","Female"))
    if gender == "Male": gender = 1 
    else: gender = 0
    res.append(gender)
    res.append(change(gender))

    columns  = ['Polyuria', 'Polydipsia', 'sudden weight loss',
       'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
       'Itching', 'Irritability', 'delayed healing', 'partial paresis',
       'muscle stiffness', 'Alopecia', 'Obesity']
    
    col_dict = dict.fromkeys(columns, 0)

    for key, val in col_dict.items():
        val = st.radio(f"Do you have {key} ?",("Yes","No"))
        val = convert(val)
        res.append(val)
        res.append(change(val))

    submitted = st.button('Submit')

    if submitted:
        res = np.array(res)
        results = model.predict([res])

        if results ==1:
            st.warning('You might have Diabeties. Please consult with a Doctor.')
        else:
            st.info("You don't have Diabeties. Please consult with Doctor for verification.")

# Run main Function
if __name__ == "__main__":
    run()