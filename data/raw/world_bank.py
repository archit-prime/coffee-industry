# data_collection.py
import requests
import pandas as pd

def get_worldbank_data(indicator, country_codes, start_year, end_year):
    url = f'http://api.worldbank.org/v2/country/{country_codes}/indicator/{indicator}?format=json&date={start_year}:{end_year}&per_page=1000'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data")
        return None

def main():
    indicator = 'NY.GDP.MKTP.CD'  # Replace this with the coffee consumption indicator code
    country_codes = 'US'
    start_year = 2017
    end_year = 2021

    data = get_worldbank_data(indicator, country_codes, start_year, end_year)

    if data:
        data_list = data[1]
        data_df = pd.DataFrame(data_list)
        data_df.to_csv('data/raw/coffee_consumption_data.csv', index=False)
        print("Data saved successfully")

if __name__ == "__main__":
    main()
