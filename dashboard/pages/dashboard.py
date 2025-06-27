import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
st.title("Titanic Dashboards")
st.write("This is the dashboard of titanic dataset")
df=sns.load_dataset("titanic")
st.dataframe(df)