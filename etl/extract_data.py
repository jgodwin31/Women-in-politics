import requests
import pandas as pd

def extract_data():
    """Fetches World Bank data on women in parliament."""
    url = "https://api.worldbank.org/v2/country/all/indicator/SG.GEN.PARL.ZS?format=json&per_page=20000"
    response = requests.get(url)
    data = response.json()[1]  # second element contains the records
    
    records = []
    for item in data:
        records.append({
            "country": item["country"]["value"],
            "country_code": item["country"]["id"],
            "year": int(item["date"]),
            "women_percentage": item["value"]
        })
    
    df = pd.DataFrame(records)
    df.to_csv("data/raw/worldbank_women_parliament.csv", index=False)
    return df
