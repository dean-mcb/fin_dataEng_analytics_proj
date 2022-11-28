################ Load stock info data into MySQL DB hosted on AWS EC2 ################

import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Create connection to mysql db on localhost
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="********",
                               pw="********",
                               db="stockapi"))

# Get overview data from csv file into pd df
overview_data_all_df = pd.read_csv(r'/home/ubuntu/overview_data_all.csv')
overview_data_all_df.drop(columns = overview_data_all_df.columns[0], axis = 1, inplace= True)
overview_data_all_df['Description'] = overview_data_all_df['Description'].str[:90]
overview_data_all_df.replace('None',np.nan, inplace=True)
overview_data_all_df.replace('-', np.nan, inplace=True)
overview_data_all_df.to_sql('overview_data_all', con = engine, if_exists = 'append',index = False, chunksize = 1000)

print('done')