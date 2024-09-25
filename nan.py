import pandas as pd 
items = [
    {"bikes" : 20, "pants" : 30, "watches":35, "shirts": 15, "shoes": 8, "suits": 45}, 
    {"watches":10, "glasses":50, "bikes":15, "pants":5, "shirts":2, "shoes" : 5, "suits":7}, 
    {"bikes": 20, "pants": 30, "watches": 35, "glasses": 4, "shoes": 10}
]
# create a data frame
store_items = pd.DataFrame(items, index=["store 1", "store 2", "store 3"])
print(store_items)

# count the (total) NaN values: 
x = store_items.isnull().sum().sum()
print("Total Number of Null values = ", x)

# count the NaN down the column: 
y = store_items.isnull().sum()
print("Number of Null values in each column = \n", y)

# count the (total) non-NaN values:
t = store_items.count()
print("Total Number of non-Null values = \n", t)

#eliminate NaN values: 
store_items.dropna(axis=0) #drop ROWS with NaN values: 
print("--- DF after dropping NaN rows ---")
# print(store_items.dropna(axis=0)) # in-place : to reflect changes in the actual DF 

store_items.dropna(axis=1) #drop Column with NaN values: 
print("--- DF after dropping NaN columns ---")
print(store_items.dropna(axis=1)) , # in-place : to reflect changes in the actual DF 

# substituting NaN values: 
# 1. replace NaN values with 0 : 
print("--- replacing the NaN values with 0 ---")
print(store_items.fillna(0))

#2. forward filling : replace NaN values with previous values the DF :
print("--- forward filling ---")
# print(store_items.fillna(method='ffill', axis=0)) # deprecated 
print(store_items.ffill(axis=0))

#2. backward filling : replace NaN values with values that go after them :
print("--- backward filling ---")
# print(store_items.fillna(method='ffill', axis=0)) # deprecated 
print(store_items.bfill(axis=0))

# estimate = interpolate NaN values down (axis 0)
print("--- interpolate NaN values (1) ---")
print(store_items.interpolate(method="linear", axis=0)) # column values
print("--- interpolate NaN values (2) ---")
print(store_items.interpolate(method="linear", axis=1)) # row values


