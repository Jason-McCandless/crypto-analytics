import requests, json

import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

IDS = "bitcoin,ethereum,solana,cardano"
CURRENCY = "gbp"
BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"
API_KEY = os.getenv("COINGECKO_API_KEY")
HEADERS = {
    "accept": "application/json",
    "X-CoinGecko-Api-Key": API_KEY
}
PARAMS = {
    "ids": IDS,
    "vs_currency": CURRENCY
}

def fetch_data():
    try:    
        print("Fetching currencies...")
        r = requests.get(BASE_URL, headers=HEADERS, params=PARAMS, timeout=10)
        r.raise_for_status()  # Raise an exception for HTTP errors
        data = r.json()
        print("Request successful with status code: ", r.status_code, " saving data")
        print(f"Retrieved {len(data)} cryptocurrencies.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    return data

def save_raw_data(data):
    with open("data/raw/data.json", "w") as f:
        json.dump(data, f, indent=4)

def main():
    data = fetch_data()
    if data:
        save_raw_data(data)

if __name__ == "__main__":
    main()