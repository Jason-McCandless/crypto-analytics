# from extract import fetch_market_data, save_raw_data
# from transform import transform_market_data

# def main():
#     data = fetch_market_data()
#     if data:
#         save_raw_data(data)
#         clean_df = transform_market_data(data)
#         print(clean_df.head())

# if __name__ == "__main__":
#     main()

from extract import fetch_market_data, save_raw_data
from transform import transform_market_data
from load import load_to_snowflake

def main():

    data = fetch_market_data()

    if data is None:
        return

    save_raw_data(data)

    clean_df = transform_market_data(data)

    if clean_df is not None:
        load_to_snowflake(clean_df)

if __name__ == "__main__":
    main()