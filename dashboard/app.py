import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

engine = create_engine("postgresql://postgres:joshipro@localhost:5432/women_politics")

st.title("🌍 Women in Politics Dashboard")
st.caption("Data source: World Bank (SG.GEN.PARL.ZS)")

df = pd.read_sql("SELECT * FROM representation", engine)

countries = sorted(df["country"].unique())
country = st.selectbox("Select a country:", countries)

filtered = df[df["country"] == country]
fig = px.line(filtered, x="year", y="women_percentage",
              title=f"{country}: Women in Parliament Over Time",
              markers=True)
st.plotly_chart(fig)

avg_fig = px.bar(df.groupby("year")["women_percentage"].mean().reset_index(),
                 x="year", y="women_percentage", title="Global Average Over Time")
st.plotly_chart(avg_fig)
