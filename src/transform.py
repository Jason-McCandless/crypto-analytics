import pandas as pd

# def transform_data(data):
#     df = pd.read_json(data)
#     print(df.to_string())
try:
    data = "data/raw/data.json"
    df = pd.read_json(data)
    if df.empty:
        print("DataFrame is empty. No data to process.")
    else:
        clean_df = df.loc[:, ]
        print(clean_df.info())
        print(clean_df.dtypes())
except Exception as e:
    print(f"Error processing data: {e}")