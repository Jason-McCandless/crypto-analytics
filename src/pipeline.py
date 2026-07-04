from extract import fetch_market_data, save_raw_data
from transform import transform_market_data

def main():
    data = fetch_market_data()
    if data:
        save_raw_data(data)
        clean_df = transform_market_data(data)
        print(clean_df.head())

if __name__ == "__main__":
    main()