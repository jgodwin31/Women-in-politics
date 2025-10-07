import pandas as pd

def transform_data(df):
    """Cleans and prepares the data for database loading."""
    df = df.dropna(subset=["women_percentage"])
    df = df[df["year"] >= 1990]  # filter to relevant modern data
    df["women_percentage"] = df["women_percentage"].round(2)
    df = df.drop_duplicates(subset=["country", "year"])
    return df
