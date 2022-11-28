############### Build Stock info CSV ###########

from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd
import time

# Get company overview data for column names
API_key = "***********"
overview = FundamentalData(key=API_key, output_format='pandas')

# Get list of all tickers from csv
list_of_all_tickers = pd.read_csv(r'/home/ubuntu/list_of_tickers.csv')
list_of_all_tickers = list(list_of_all_tickers.symbol)

# Get all company overview data into df
overview_data_all = pd.read_csv(r'/home/ubuntu/overview_data_all.csv',index_col=(0))
openingtickercount = len(list(overview_data_all.Symbol))

# Get current tickers
current_tickers = list(overview_data_all.Symbol)

# Get remaining tickers
remaining_tickers = set(list_of_all_tickers) - set(current_tickers)

# Get remaining overview data
for ticker in remaining_tickers:

    print('getting ticker:', ticker)
    try:
        overviewdata = overview.get_company_overview(ticker)
    except ValueError:
        print('ValueError')
        continue
    except:
        break

    overview_data_all = pd.concat([overview_data_all,overviewdata[0]], ignore_index = True)
    print(ticker,': saved')
    time.sleep(20)
    if len(list(overview_data_all.Symbol)) - openingtickercount > 20:
        break

# Write to file
overview_data_all.to_csv(r'/home/ubuntu/overview_data_all.csv')



print('ALL DONE !!!!')