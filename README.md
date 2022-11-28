# fin_dataEng_analytics_proj
A data engineering, ETL and analytics project, using data through an API connection from alphaVantage and ending at a PowerBI desktop dashboard.

Pre-requisites:
1. MySQL DB has been set up (called stockapi)...localhost, in the cloud, where ever.

ETL:
1. Visit www.alphavantage.co and sign-up for your own API key
2. Insert the API key into the file getListingStatus.py and then Run. This script will extract 'listing status' data from the api and insert into a new table in the 'stockapi' db in MySQL
3. Insert MySQL db username and password parameters into the getListofTickers.py file, and then Run. Modify file to include/exclude security exchanges (i.e. NYSE, NASDAQ, etc.) if/as required.
4. Insert api key into initializeStockInfoFile.py and then Run.
5. Insert api key into build_stock_info.py and save.
6. Open crontab -e and edit, so that the build_stock_info.py file is run automatically as often as is required. (If using the free version of alphavantage api, there are limitations to the data extracts, which can be found on their website). Use the crontabConfig.txt as an example. This exercise will build a file called 'overview_data_all.csv' with stock info data from all the tickers, specified in the 'list_of_tickers.csv' file, that was created in point 3 above.
7. Create a new table in the stockapi db called 'overview_data_all'. Ensure it has all the relevant columns that exist in the 'overview_data_all.csv' file.
8. Once the 'overview_data_all.csv' file has all the data, edit the loadDataIntoMySQLdb.py by inserting the db username and password parameters for the MySQL db instance, and then Run. Some troubleshooting may be required.
9. All data should now be in the 'overview_data_all' database table.

Data analytics and BI
1. Open PowerBI (Desktop)
2. Go to 'Get Data' and select 'MySQL database' and select 'Connect'.
3. Enter the server details and the database name (i.e. 'stockapi')
4. If required ensure the correct credentials are supplied.
5. Start creating your analytics dashboard.
