import streamlit as st
import pandas as pd


df = pd.DataFrame({'col1':[1,2,11]})

st.dataframe(df)