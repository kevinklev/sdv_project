import pandas as pd
import streamlit as st
import plotly.express as px


cars_df = pd.read_csv('vehicles_us.csv')


cars_df.rename(columns = {'type': 'vehicle_type'})
cars_df['manufacturer']= cars_df['model'].apply(lambda x: x.split()[0])



st.header('Market Trends for Online Car Ads')

st.write("""
#### Filter to include salvage cars in data.
""")

show_salvage_cars = st.checkbox('Include salvage cars in data')



if not show_salvage_cars:
    cars_df = cars_df[cars_df.condition != 'salvage']



st.write("""
   ### Distribution of Number of Days Listed on Ad Space
    """)

list_for_hist = ['transmission', 'fuel', 'condition', 'cylinders']
choice_for_hist = st.selectbox('Distribution of days on adspace based on:', list_for_hist)

days_hist = px.histogram(cars_df, x = 'days_listed', color = choice_for_hist)
st.write(days_hist)



st.write("""
    ### Scatterplot of Price versus Model Year
    """)
list_for_scatter = ['transmission', 'fuel', 'condition']
choice_for_scatter = st.selectbox('Price versus Model Year based on:', list_for_scatter)

price_manu = px.scatter(cars_df, y = 'price', x = 'model_year', title = 'Scatterplot of Prices by Model Year After 1950', color = choice_for_scatter)
price_manu.update_layout(yaxis_range=[0,200000])
price_manu.update_layout(xaxis_range=[1950, 2019])

st.write(price_manu)