import streamlit as st
import pandas as pd
import numpy as np
import pickle



# months       - total number of months in service
# phones       - Number of handsets issued
# attempt_Mean - mean number of attempted calls
# actvsubs     - Number of customer who are actively using the service in the same household
# dualband     - a dual band device enables broader roaming capabilities to users
# area         - Geogrpahic area user located area



st.set_page_config(layout="wide")

filename = 'model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

st.title('Customer Churn Prediction')
st.write('This is a web app to predict whether the customer is going to churn or not?')
dualband_Y = 0
dualband_N = 0
dualband_T = 0


# area_NEW_YORK_CITY_AREA = 0
# area_DC_MARYLAND_VIRGINIA_AREA = 0

with st.sidebar:
    months         = st.number_input(label='Number of Months',min_value = 0,
                        max_value = 70,
                        value = 6,
                        step = 1)      

    phones         = st.slider(label = 'Number of handset issued', min_value = 0,
                        max_value = 30,
                        value = 1,
                        step = 1)

    attempted_calls    = st.number_input(label='Number of Attempted calls', min_value = 0.0,
                        max_value = 2500.0,
                        value = 0.0,
                        step = 50.0)      


    active_household_members    = st.number_input(label='Active number of customers in same household', min_value = 1,
                        max_value = 60,
                        value = 1,
                        step = 1)   
  

    dualband   = st.radio('Dualband', ('Yes','No','Yes (With Tri-Band)'))
    if (dualband == 'Yes'):
        dualband_Y = 1
    elif (dualband == 'No'):
        dualband_N = 1
    else:
        dualband_T = 1

    # area = st.selectbox(
    #     'User located area',
    #     ('NEW YORK CITY AREA', 'DC/MARYLAND/VIRGINIA AREA'))
    # if (area == 'NEW YORK CITY AREA'):
    #     area_NEW_YORK_CITY_AREA = 1
    # else:
    #     area_DC_MARYLAND_VIRGINIA_AREA = 1

       

    # st.write('You selected:', area)    

    # automatic   = st.checkbox('Automatic')

    # gears   = st.radio('Gears', ('4','5','6'))

features = {
  'months':months,
  'phones':phones,
  'attempted_calls': attempted_calls,
  'active_household_members':active_household_members,
  'dualband_Y':dualband_Y,
   'dualband_N':dualband_N,
  'dualband_T':dualband_T,
#   'area':	area
  }
  

features_df  = pd.DataFrame([features])

st.table(features_df)
col1, col2 = st.columns((1,2))

with col1:
    prButton = st.button('Predict')
with col2: 
    if prButton:    
        prediction = loaded_model.predict(features_df) 
        if int(prediction) == 0:
            st.subheader('Customer will continue to use the service.')
        else: 
            st.subheader('Customer is going to stop using the service.')