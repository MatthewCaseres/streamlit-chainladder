import streamlit as st
import pandas as pd
import chainladder as cl

st.markdown("# Hosting actuarial dashboards in Streamlit")
st.markdown("Here is the top 10 rows from a big rectangle of data. We want to get triangles from this rectangle.")
n=10
@st.cache_data(ttl=3600*10)
def get_data():
    return pd.read_csv(
        "https://raw.githubusercontent.com/casact/chainladder-python/master/chainladder/utils/data/clrd.csv"
    )
clrd_df = get_data()
clrd_df_head = clrd_df.head(n)
clrd_df_head
st.markdown("""Casualty actuaries create reports with \"loss triangles\". 
For the triangles we use the [chainladder-python](https://chainladder-python.readthedocs.io/en/latest/intro.html) package. This package is published by the Casualty Actuarial Society and is
the [most popular open source actuarial project ever](https://www.actuarialopensource.org/).""")
st.markdown("""We host the loss triangles on the web using streamlit, the [most popular open source python package for hosting dashboards](https://star-history.com/#streamlit/streamlit&plotly/dash&rstudio/shiny&Date).""")

clrd = cl.Triangle(
    clrd_df,
    origin="AccidentYear",
    development="DevelopmentYear",
    columns=[
        "IncurLoss",
        "CumPaidLoss",
        "BulkLoss",
        "EarnedPremDIR",
        "EarnedPremCeded",
        "EarnedPremNet",
    ],
    index="LOB",
    cumulative=True,
)

st.write("Selectors")

lob = st.selectbox("Line of Business", clrd.index)

column = st.selectbox("Type", clrd.columns)

triangle = clrd.loc[lob, column]

st.markdown("This is a triangle for " + lob + " and " + column + ".")

triangle

st.markdown("This is a heatmap of the link ratio.")

st.write(triangle.link_ratio.heatmap())