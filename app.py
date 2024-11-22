import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

import datetime

d = st.date_input(
    "date?",
    datetime.date(2019, 7, 6))
st.write('date is:', d)

import datetime

t = st.time_input('time', datetime.time(8, 45))

st.write('time', t)

number2 = st.number_input('Insert pickup longitude')

st.write('The pickup longitude is ', number2)

number3 = st.number_input('Insert pickup latitude')

st.write('The pickup latitude is ', number3)

number4 = st.number_input('Insert dropoff longitude')

st.write('The dropoff longitude is ', number4)

number5 = st.number_input('Insert dropoff latitude')

st.write('The dropoff latitude is ', number5)

number6 = st.number_input('Insert passenger count')

st.write('The passenger count is ', number6)

import requests
data = requests.get("'https://taxifare.lewagon.ai/predict'").json()

st.write(data)
