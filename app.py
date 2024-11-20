import streamlit as st
import pandas as pd
import numpy as np

from  src.pipeline.predict_pipeline import CustomData , PredictPipeline
# 
import os

st.title("Student Performance Prediction App")

st.subheader("Predict the math score of a student based on various Features")

st.markdown("""
            Fill in the details below and click **Predict** to estimate the student's math score .
            """)

st.markdown('------')

col1 ,col2 =st.columns(2)


# input fields in the first column
with col1:
    gender = st.selectbox('Gender', ['male', 'female'])
    parental_level_of_education = st.selectbox(
        "Parental Level of Education", [
            'some high school',
            'high school',
            'some college',
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )
    test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])
    reading_score = st.number_input('Reading Score', min_value=0.0, max_value=100.0, step=0.5)

# Input fields in the second column
with col2:
    race_ethnicity = st.selectbox(
        'Race/Ethnicity', [
            'group A', 'group B', 'group C', 'group D', 'group E'
        ]
    )
    lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])
    writing_score = st.number_input('Writing Score', min_value=0.0, max_value=100.0, step=0.5)


# predict button

if st.button("Predict"):


    data=CustomData( gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )


    #convert input data as df

    pred_df = data.get_data_as_data_frame()
    st.markdown("#### Input Data :")
    st.write(pred_df)


    # intialize the prediction pipeline and make prediction
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)


    st.markdown('###Prediction Results')
    st.success(f"The Preidcted math score is : **{results[0]:.2f}**")


# add a footer
st.markdown('-----')
st.caption("Developed By Sandesh")