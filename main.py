import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Simple Data dashboard!")

uploaded_file =st.file_uploader("Choose a CSV file",type ="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe( ))

    st.subheader("Filter")
    columns =  df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by",columns)
    unique_values = df[selected_column].unique()
    select_value = st.selectbox("Select value",unique_values) 

    filtered_df = df[df[selected_column]== select_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x-column",columns)
    y_column = st.selectbox("select y-column",columns)
    
    if st.button("Genrate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else :
    st.write("waiting for file upload!")
