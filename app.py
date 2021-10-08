"""Main App logic for prediction."""
import streamlit as st
import numpy as np
import pandas as pd
from joblib import load


# Load Model 
model = load('model_health')

# Main function that holds logic
def run():

    # Display Bean Icon and title
    st.title('Diabetes Prediction App')
    st.image('image.jpg', use_column_width=True)
    st.subheader("Fill in the questions and click on the button below.")

    age = st.number_input("What is your Age?")
    gender = st.radio("What is your Gender?",("Male","Female"))
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
    
    polyuria = st.radio("Do you have Polyuria?",("Yes","No"))
    if polyuria == 'Yes':
        polyuria = 1
    else:
        polyuria = 0
    
    polydipsia = st.radio("Do you have Polydipsia?",("Yes","No"))
    if polydipsia == 'Yes':
        polydipsia = 1
    else:
        polydipsia = 0
    
    weight = st.radio("Recently do you observe sudden weight loss?",("Yes","No"))
    if weight == 'Yes':
        weight = 1
    else:
        weight = 0
    
    weakness = st.radio("Do you feel any Weekness?",("Yes","No"))
    if weakness == 'Yes':
        weakness = 1
    else:
        weakness = 0
    
    polyphagia = st.radio("Do you have Polyphagia?",("Yes","No"))
    if polyphagia == 'Yes':
        polyphagia = 1
    else:
        polyphagia = 0
    
    genital_thrush = st.radio("Do you have Genital thrush?",("Yes","No"))
    if genital_thrush == 'Yes':
        genital_thrush = 1
    else:
        genital_thrush = 0
    
    visual_blurring = st.radio("Do you have Visual blurring?",("Yes","No"))
    if visual_blurring == 'Yes':
        visual_blurring = 1
    else:
        visual_blurring = 0
    
    itching = st.radio("Do you have Itching?",("Yes","No"))
    if itching == 'Yes':
        itching = 1
    else:
        itching = 0
    
    irritability = st.radio("Do you have Irritability?",("Yes","No"))
    if irritability == 'Yes':
        irritability = 1
    else:
        irritability = 0
    
    delayed_healing = st.radio("Do you have Delayed healing?",("Yes","No"))
    if delayed_healing == 'Yes':
        delayed_healing = 1
    else:
        delayed_healing = 0
    
    partial_paresis = st.radio("Do you have Partial paresis?",("Yes","No"))
    if partial_paresis == 'Yes':
        partial_paresis = 1
    else:
        partial_paresis = 0
    
    muscle_stiffness = st.radio("Do you have Muscle stiffness?",("Yes","No"))
    if muscle_stiffness == 'Yes':
        muscle_stiffness = 1
    else:
        muscle_stiffness = 0

    alopecia = st.radio("Do you have Alopecia?",("Yes","No"))
    if alopecia == 'Yes':
        alopecia = 1
    else:
        alopecia = 0
    
    obesity = st.radio("Do you have Obesity?",("Yes","No"))
    if obesity == 'Yes':
        obesity = 1
    else:
        obesity = 0

    row = [age,gender,polyuria,polydipsia,weight,weakness,polyphagia,genital_thrush,visual_blurring,itching,irritability, delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity]

    row = np.array(row)
    

    if st.button("Predict"):

        result = model.predict(row)
        if True:
            st.warning('You might have Diabeties. Please consult with a Doctor.')
        else:
            st.success("You don't have Diabeties. Please consult with Doctor for verification.")


# Main Function
if __name__ == "__main__":
    run()




    """polyuria = st.radio("Do you have Polyuria?",("Yes","No"))
    polydipsia = st.radio("Do you have Polydipsia?",("Yes","No"))
    weight = st.radio("Recently do you observe sudden weight loss?",("Yes","No"))
    weakness = st.radio("Do you feel any Weekness?",("Yes","No"))
    polyphagia = st.radio("Do you have Polyphagia?",("Yes","No"))
    genital_thrush = st.radio("Do you have Genital thrush?",("Yes","No"))
    visual_blurring = st.radio("Do you have Visual blurring?",("Yes","No"))
    itching = st.radio("Do you have Itching?",("Yes","No"))
    irritability = st.radio("Do you have Irritability?",("Yes","No"))
    delayed_healing = st.radio("Do you have Delayed healing?",("Yes","No"))
    partial_paresis = st.radio("Do you have Partial paresis?",("Yes","No"))
    muscle_stiffness = st.radio("Do you have Muscle stiffness?",("Yes","No"))
    alopecia = st.radio("Do you have Alopecia?",("Yes","No"))
    obesity = st.radio("Do you have Obesity?",("Yes","No"))"""""