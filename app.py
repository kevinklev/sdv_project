import pandas as pd
import streamlit as st
import plotly.express as px

cars_df = pd.read_csv('vehicles_us.csv')

cars_df.rename(columns = {'type': 'vehicle_type'})
cars_df['manufacturer']= cars_df['model'].apply(lambda x: x.split()[0])

age = cars_df['model_year']

rel_age = []
for i in age:
    if i > 2014:
        rel_age.append('< 5 years')
    elif 2014 >= i >2009 :
        rel_age.append('6-10 years')
    elif 2009 >= i >2004 :
        rel_age.append('11-15 years')
    elif 2004 >= i > 1998:
        rel_age.append('16-20 years')
    elif i <=1998:
        rel_age.append('20+ years')
    else:
        rel_age.append('unknown')
cars_df['vehicle_age'] = rel_age 

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

list_for_hist = ['transmission', 'fuel', 'condition']
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

st.write("""
    ### Ford vs Chevrelot on Adspace
    """)

st.write("""
    ##### Totals only reflect counts for Ford and Chevrolet vehicles
    """)

ford_chev_list = ['chevrolet', 'ford']
ford_chev = cars_df[cars_df.manufacturer.isin(ford_chev_list)]


choice = ford_chev['manufacturer'].unique()
choice_for_man = st.selectbox('Select manufacturer:', choice)

filtered_data = cars_df[cars_df.manufacturer == choice_for_man]

list_type = ['fuel', 'condition', 'type']
choice_for_type = st.selectbox('Based on:', list_type)


fc_graph = px.bar(filtered_data, x = 'vehicle_age', color = choice_for_type, title = f'Bar Chart of Data for {choice_for_man.title()} vehicles:')
st.write(fc_graph)


## hey there! I think I applied all the changes and all of the filters seem to be working when I run it on mine.
## If something continues not to work, can you be a bit more specific in feedback
## as to what specifically needs to be fixed. Thank you! 
