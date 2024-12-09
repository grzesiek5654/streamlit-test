import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Polecenie st.write')

# Przykład 1

st.write('Witaj, *Świecie!* :sunglasses:')

# Przykład 2

st.write(1234)

# Przykład 3

df = pd.DataFrame({
     'pierwsza kolumna': [1, 2, 3, 4,5],
     'druga kolumna': [10, 20, 30, 40,50]
     })
st.write(df)

# Przykład 4

st.write('Poniżej znajduję ramka danych:', df, 'Powyżej znajduje się ramka danych.')

# Przykład 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)