import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AI Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("AI-Based Air Quality Monitoring Dashboard")

df = pd.read_csv("air_quality.csv")

st.subheader("Air Quality Dataset")

st.write("Dataset Shape:", df.shape)

st.dataframe(df.head(10))

st.subheader("Dataset Information")
st.write(df.describe())

st.subheader("Air Quality Visualization")

numeric_columns = df.select_dtypes(include=np.number).columns

if len(numeric_columns) > 0:
    selected_column = st.selectbox(
        "Select parameter",
        numeric_columns
    )

    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], kde=True, ax=ax)
    st.pyplot(fig)
else:
    st.warning("No numeric columns found in dataset.")
