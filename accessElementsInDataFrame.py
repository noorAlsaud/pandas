import pandas as pd
# Accessing Elements in pandas DataFrames
items = [
    {"bikes" : 20, "pants" :30, "watches" : 35}, 
    {"watches" : 10, "glasses" : 50, "bikes" : 15, "pants" : 5}
    ]
store_items = pd.DataFrame(items, index=["store 1", "store 2"])
print("--- store_items ---")
print(store_items)
print("------")
print("store_items : bike\n", store_items[["bikes"]])
print("------")
print("store 1", store_items.loc[["store 1"]])

# add new column "shirts"
store_items["shirts"] = [15, 2]
print("------")
print(store_items)

# add new column using arithmetic operations: 
store_items["suits"] = store_items["shirts"] + store_items["pants"]
print("------")
print(store_items)
print("------")

# create a row in dataFrame - 1. create new DF 2. append()
new_items = [{"bikes": 20, "pants": 30, "watches":35, "glasses":4}]
new_store = pd.DataFrame(new_items, index=["store 3"])
print("--- new store ----")
print(new_store)
print("--- new store lists 1,2,3 ----")
store_items = pd.concat([store_items, new_store], ignore_index=True) #   append() is dupricated
print(store_items)

#delete one column from a dataframe : 
store_items.pop("suits")
print(store_items)

#delete mutiple columns from a dataframe Pop() & drop() : 
store_items = store_items.drop(['watches' ,'shoes'], axis=1)
print(store_items)