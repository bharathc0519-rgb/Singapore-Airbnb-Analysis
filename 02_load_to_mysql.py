"""
Load listings_cleaned.csv directly into MySQL using Python.
This bypasses MySQL Workbench's Table Data Import Wizard, which has a
known bug silently truncating imports on larger CSV files.
"""
import pandas as pd
from sqlalchemy import create_engine

# ---------------------------------------------------------
# UPDATE THESE with your MySQL credentials
# ---------------------------------------------------------
MYSQL_USER = "root"
MYSQL_PASSWORD = "1234"   # <-- change this
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "singapore_airbnb"

# ---------------------------------------------------------
# Load CSV
# ---------------------------------------------------------
df = pd.read_csv("listings_cleaned.csv")
print(f"Loaded CSV: {df.shape[0]} rows, {df.shape[1]} columns")

# ---------------------------------------------------------
# Connect to MySQL and push the data
# ---------------------------------------------------------
connection_str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(connection_str)

df.to_sql(
    name="listings",
    con=engine,
    if_exists="replace",   # drops and recreates the table cleanly
    index=False,
    chunksize=500          # insert in batches, avoids single giant query
)

print("Upload complete!")

# ---------------------------------------------------------
# Verify
# ---------------------------------------------------------
with engine.connect() as conn:
    result = conn.exec_driver_sql("SELECT COUNT(*) FROM listings")
    count = result.fetchone()[0]
    print(f"Rows in MySQL 'listings' table: {count}")
