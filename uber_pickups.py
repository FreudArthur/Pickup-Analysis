import streamlit as st
import pandas as pd
import numpy as np


st.title('Uber pickups au NYC')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

with st.spinner("Chargement des données ... "):
    data = load_data(10000)
st.success("(10000 lignes chargées 🔥 ...)")


if st.checkbox('Voir les données data'):
    st.subheader('Données ')   
    st.write(data)


st.subheader('Nombre de pickups par heure')


hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Carte de toutes les pickups')


st.map(data)

hour_to_filter = st.slider('Heure', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Carte de toutes les pickups {hour_to_filter}:00')
st.map(filtered_data)

