#Extracting the Actual Stock Prices of Jan-2017.


dataset_test = pd.read_csv("Google_Stock_Price_Test.csv")
Actual_stock_price =  dataset_test.iloc[ : , 1:2 ].values
