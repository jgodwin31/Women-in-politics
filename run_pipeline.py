from etl import extract_data, transform_data, load_data

if __name__ == "__main__":
    print("🔹 Extracting data...")
    df = extract_data()
    print("🔹 Transforming data...")
    clean_df = transform_data(df)
    print("🔹 Loading data...")
    load_data(clean_df)
    print("✅ Pipeline completed successfully!")
