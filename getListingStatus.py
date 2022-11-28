###### Acquire stock listing status ##############

import csv
import requests
import pandas as pd
from sqlalchemy import create_engine

URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=********'
r = requests.get(URL)
df = pd.read_csv(URL)

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="********",
                               pw="********",
                               db="stockapi"))


df.to_sql('listing_status', con = engine, if_exists = 'replace',index = True)

print('done')