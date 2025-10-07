import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Step 3: Connect to PostgreSQL
engine = create_engine("postgresql://postgres:joshipro@localhost:5432/women_politics")

# Step 4: Load data
@st.cache_data
def load_data():
    query = "SELECT * FROM representation"
    df = pd.read_sql(query, engine)
    return df

df = load_data()

# Step 4 continued: Title and preview
st.title("🌍 Women in Politics Dashboard")
st.write("Global trends of women in political representation.")
st.dataframe(df.head(10))

# Step 5: Filter by country
countries = df['Country Name'].unique()
selected_country = st.selectbox("Select a country:", countries)

filtered_df = df[df['Country Name'] == selected_country]
st.write(f"Showing data for {selected_country}")
st.dataframe(filtered_df)

# Step 6: Line chart over time
fig = px.line(
    filtered_df,
    x="Year",
    y="Value",
    title=f"Women in Parliament (%) — {selected_country}",
    markers=True
)
st.plotly_chart(fig)

# Step 7: Global comparison map
year = st.slider("Select Year:", int(df['Year'].min()), int(df['Year'].max()), int(df['Year'].max()))

year_df = df[df['Year'] == year]
fig_map = px.choropleth(
    year_df,
    locations="Country Code",
    color="Value",
    hover_name="Country Name",
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f"Women in Parliament (%) — {year}"
)
st.plotly_chart(fig_map)
