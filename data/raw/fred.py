# src/data_collection/collect_data.py
import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv

load_dotenv()

FRED_API_KEY = os.getenv('FRED_API_KEY')
FRED_BASE_URL = 'https://api.stlouisfed.org/fred'
DATA_DIR = 'data/raw'

def get_fred_data(series_id, api_key):
    url = f"{FRED_BASE_URL}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return pd.DataFrame(data['observations'])
    else:
        print(f"Failed to fetch data for {series_id}")
        return None

def main():
    # Example: get coffee price data from FRED
    series_id = 'PCOFFOTMUSDM'  # Replace with the relevant series ID
    coffee_prices = get_fred_data(series_id, FRED_API_KEY)
    
    if coffee_prices is not None:
        coffee_prices.to_csv(os.path.join(DATA_DIR, 'coffee_prices.csv'), index=False)

if __name__ == '__main__':
    main()
