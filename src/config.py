import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))

REQUIRED_COLUMNS = ['id', 
                    'symbol', 
                    'name', 
                    'current_price', 
                    'market_cap', 
                    'market_cap_rank', 
                    'total_volume', 
                    'price_change_percentage_24h', 
                    'circulating_supply', 
                    'last_updated'
                ]
IDS = "bitcoin,ethereum,solana,cardano"
CURRENCY = "gbp"

SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
}