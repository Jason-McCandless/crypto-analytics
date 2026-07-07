import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

from config import SNOWFLAKE_CONFIG

def get_connection():

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"],
        role=SNOWFLAKE_CONFIG["role"]
    )

    return conn


def load_to_snowflake(df):

    if df.empty:
        raise ValueError("DataFrame is empty.")

    conn = get_connection()

    try:

        success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        table_name="CRYPTO_MARKET_DATA",
        quote_identifiers=False,
        use_logical_type=True
        )

        if not success:
            raise RuntimeError("Snowflake load failed.")

        print(f"Loaded {nrows} rows in {nchunks} chunk(s).")

    finally:
        conn.close()

