import pandas as pd
from config import REQUIRED_COLUMNS
from extract import fetch_data

# def transform_data(data):
#     df = pd.read_json(data)
#     print(df.to_string())
def transform_data(data):
    df = pd.DataFrame(data)
    # check df.columns to ensure it contains all REQUIRED_COLUMNS
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    duplicates = df["id"].duplicated().sum()
    if duplicates > 0:
        print(f"Found {duplicates} duplicate entries.")
        raise ValueError("Duplicate entries found in the data.")
    else: 
        print ("No duplicate entries found.")
    if df.empty:
        print("DataFrame is empty. No data to process.")
        return None
    else:
        clean_df = df.loc[:, REQUIRED_COLUMNS]
        # convert last_updated to datetime
        clean_df["last_updated"] = pd.to_datetime(clean_df["last_updated"], errors='coerce')
        # add ingestion timestamp
        clean_df["ingestion_timestamp"] = pd.Timestamp.now()

        print(clean_df.info())
        print(clean_df.dtypes)
        return clean_df
