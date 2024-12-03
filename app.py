import streamlit as st
import pickle
import pandas as pd

with open('Model_Daegu_Apartment.pkl', 'rb') as f:
    model = pickle.load(f)

def calculator(hallway_type, time_to_subway, subway_station, no_facilities_nearby, no_public_offices, no_universities, no_parking_lots, year, no_facilities_inside, unit_area):
    data = pd.DataFrame({
        'Hallway Type': [hallway_type], 
        'Time To Subway St.': [time_to_subway],
        'Subway Station': [subway_station],
        'No. Facilities Nearby': [no_facilities_nearby],
        'No. Public Offices Nearby': [no_public_offices],
        'No. Universities Nearby': [no_universities],
        'No. Parking Lots': [no_parking_lots],
        'Year Built': [year],
        'No. Facilities Inside': [no_facilities_inside],
        'Unit Area (sqft)': [unit_area],
    })
    
    prediction = model.predict(data)
    return prediction[0]

st.title("Daegu Apartment Price Calculator")

st.write("""
    This app will help you to calculate your desired to be sold apartment.
""")

hallway_type = st.selectbox('Hallway Type', ['Corridor', 'Mixed', 'Terraced'])
time_to_subway = st.selectbox('Time To Subway Station', ['No Stations Nearby', '0 - 5 min', '5 min - 10 min', '10 min - 15 min', '15 min - 20 min'])
if (time_to_subway == 'No Stations Nearby'):
    time_to_subway = 0
elif (time_to_subway == '0 - 5 min'):
    time_to_subway = 4
elif (time_to_subway == '5 - 10 min'):
    time_to_subway = 3
elif (time_to_subway == '10 - 15 min'):
    time_to_subway = 2
else:
    time_to_subway = 1
subway_station = st.selectbox('Subway Station', ['No Stations Nearby', 'Kyungbuk', 'Chilsung', 'Bangoge', 'Sinnam', 'Banwoldang', 'Myungduk', 'Daegu'])
no_facilities_nearby = st.slider('No. Facilities Nearby', 0, 10, 0)
no_public_offices = st.slider('No. Public Offices Nearby', 0, 10, 0)
no_universities = st.slider('No. Universities Nearby', 0, 5, 0)
no_parking_lots = st.slider('No. Parking Lots', 0, 1500, 500)
year = st.slider('Year Built', 1964, 2024, 2016)
no_facilities_inside = st.slider('No. Facilities Inside', 0, 10, 0)
unit_area = st.slider('Unit Area in sqft', 0, 2100, 1000)

if st.button('Calculate'):
    prediction = calculator(hallway_type, time_to_subway, subway_station, no_facilities_nearby, no_public_offices, no_universities, no_parking_lots, year, no_facilities_inside, unit_area)
    st.success(f'Best you can sell is KRW {round(float(prediction), 2)}')