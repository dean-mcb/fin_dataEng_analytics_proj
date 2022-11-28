############### Initilize the stock info CSV #########################

from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd
import csv
import requests
import time

API_key = "********"

# Get list of tickers from csv
list_of_tickers = pd.read_csv(r'/home/ubuntu/list_of_tickers.csv')
list_of_tickers = list(list_of_tickers.symbol)

# Get company overview data for column names
overview = FundamentalData(key=API_key, output_format='pandas')

tempdata = overview.get_company_overview('AAPL')[0]
list_of_columns = tempdata.columns

# Empty dataframe
overview_data_all = pd.DataFrame(columns=list_of_columns)

# 1st entry
tempdata = overview.get_company_overview(list_of_tickers[0])
overview_data_all = pd.concat([overview_data_all,tempdata[0]], ignore_index = True)

# Write to file
overview_data_all.to_csv(r'/home/ubuntu/overview_data_all.csv')

print('ALL DONE !!!!')