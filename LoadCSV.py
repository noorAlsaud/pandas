import pandas as pd 
# loading data from CSVs files = Comma Separated Values:
google_stock = pd.read_csv('./GOOG-1.csv')

# print some info : 
print('Google_stock is of type:', type(google_stock))
print('Google_stock has shape:', google_stock.shape)
# print(google_stock)

# Look at the first 5 rows in the file: 
print(google_stock.head())

# Look at the last 5 rows in the file: 
print(google_stock.tail())

# Check if any column contains a NaN. Returns a boolean for each column label
print(google_stock.isnull().any())

# getting descriptive statistics of the DF: 
print("--- describe ---")
print(google_stock.describe())

# getting descriptive statistics of one of the column in the DF: 
print("--- describe ---")
print(google_stock["Adj Close"].describe())
print('Maximum values of each column:\n', google_stock.max())
print()
print('Minimum Close value:', google_stock['Close'].min())
print()
print('Average value of each column:\n', google_stock.mean())