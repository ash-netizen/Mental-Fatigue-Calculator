import streamlit as st
import tensorflow as tf
from PIL import Image 
import numpy as np
import ktrain
from footer_utils import image, link, layout, footer


from numpy import array

import pandas as pd
from tensorflow import keras
predictor = ktrain.load_predictor('Predictor')

st.title("Mental Fatigue Calculator")
st.write("Workplaces that promote mental health and support people with mental disorders are more likely to reduce absenteeism,increase productivity and benefit from associated economic gains")
image = Image.open("IMG_2605.JPG")
st.image(image, use_column_width=True)

WFH_Setup_Available =  st.selectbox(
    'is Work from home enabled for you?',
    ('Yes', 'No')
)
Designation = st.text_input("what is your designation?")
Company_Type = st.selectbox(
    'What is your Company Type?',
    ('Product', 'Service')
)
Average_hours_worked_per_day = st.text_input("how many hours you work on an average per day?")
Employee_satisfaction_score = st.text_input("Please enter your satisfaction score on scale of 10")

data = {'WFH_Setup_Available':WFH_Setup_Available,'Designation':Designation, 'Company_Type':Company_Type, 
        'Average_hours_worked_per_day': Average_hours_worked_per_day, 'Employee_satisfaction_score': Employee_satisfaction_score}

data = pd.DataFrame([data])

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

st.write(":thinking_face:")
@st.cache
def mental_fatigue_score(WFH_Setup_Available, Designation, Company_Type, Average_hours_worked_per_day, Employee_satisfaction_score):
  prediction = predictor.predict(data)
  if prediction <= 0.3:
    prediction = 'have Excellent Mental Health, You might want to collaborate more!'
  elif 0.3 < prediction < 0.5:
    prediction = "need to work a bit on your Mental Health, Please follow https://community.virginpulse.com/work-from-home-exercises-to-keep-employees-active-and-healthy"
  elif 0.5 < prediction < 0.7:
    prediction = 'have poor Mental health, Please work on it, you can follow  https://www.mhanational.org/31-tips-boost-your-mental-health'
  else:
    prediction = 'have serious Mental issues, Please ring a bell and start to take care of your Mental Health, you can start with https://healthblog.uofmhealth.org/health-management/6-ways-to-relieve-your-work-from-home-fatigue'

  print(prediction)
  return prediction

def Score():
  Score = predictor.predict(data)
  return Score

  

if st.button("Predict"):
    result1 = Score()
    st.success('Your Mental Fatigue Score is {}'.format(int(result1*100)))
    result= mental_fatigue_score(WFH_Setup_Available, Designation, Company_Type, Average_hours_worked_per_day, Employee_satisfaction_score)
    st.success('You {}'.format(result))

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)


