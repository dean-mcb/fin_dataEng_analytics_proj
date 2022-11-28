############### Connect to MySQL on EC2 to get the list of tickers ###################

import requests
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine


# Connect
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:3306/{db}"
                       .format(user="********",
                               pw="********",
                               db="stockapi"))

# Extract data set through SQL query
# List of tickers
sql = """select *
from listing_status
where assetType = 'Stock' and exchange = 'NYSE'"""
df = pd.read_sql(sql,con=engine)
list_of_tickers = df.symbol
list_of_tickers.to_csv(index = False)

# Write to file
list_of_tickers.to_csv(r'/home/ubuntu/list_of_tickers.csv')
