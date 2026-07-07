import pandas as pd
from config import REQUIRED_COLUMNS

def transform_market_data(data):
    df = pd.DataFrame(data)
    if df.empty:
        print("DataFrame is empty. No data to process.")
        return None
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
    clean_df = df.loc[:, REQUIRED_COLUMNS].copy()
    clean_df.rename(
    columns={
        "id": "coin_id",
        "current_price": "current_price_gbp",
    },
    inplace=True
    )
    # convert last_updated to datetime
    clean_df["last_updated"] = pd.to_datetime(clean_df["last_updated"], errors='coerce')
    # check any NaT values in last_updated
    if clean_df["last_updated"].isna().any():
        print("Warning: Some 'last_updated' values could not be converted to datetime and are set as NaT.")
        raise ValueError("Invalid 'last_updated' values found in the data.")
    # add ingestion timestamp
    clean_df["ingestion_timestamp"] = pd.Timestamp.now(tz='UTC')
    return clean_df
