import streamlit as st
import pandas as pd
import time

st.write("# My First App")


st.write("## Second Header")

df = pd.read_csv("ds_salaries_clean.csv")
st.line_chart(df["Salary_USD"])


with st.sidebar:
    
    st.line_chart(df["Salary_USD"])
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

tab1, tab2, tab3 = st.tabs(["Mushuk", "Kuchuk", "Boyo'gli (Boyqush)"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   
   st.line_chart(df["Salary_USD"])

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
