import streamlit as st
from datetime import time, datetime

st.header('Polecenie st.slider')

# Przykład 1

st.subheader('Suwak')

age = st.slider('Ile masz lat?', 0, 130, 25)
st.write("Mam ", age, 'lat')

# Przykład 2

st.subheader('Suwak z zakresem')

values = st.slider(
     'Wybierz zakres wartości',
     0.0, 100.0, (25.0, 75.0))
st.write('Wybrany zakres:', values)

# Przykład 3

st.subheader('Suwak z zakresem czasu')

appointment = st.slider(
     "Zaplanuj wizytę:",
     value=(time(11, 30), time(12, 45)))
st.write("Jesteś umówiony na:", appointment)

# Przykład 4

st.subheader('Suwak z datą i czasem')

start_time = st.slider(
     "Kiedy zaczynasz?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Czas rozpoczęcia:", start_time)