import pandas as pd 
# Data Structures in Pandas (2) : Pandas Series & Pandas DataFrame

# can hold more than one data type, and assign labels for its values
groceries = pd.Series(data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"])
print(groceries) 
print("groceries has shape = ", groceries.shape)
print("groceries has dimention = ", groceries.ndim)
print("groceries has total of = ", groceries.size , " elements. ")
print("---")
print("the data in groceries is: ", groceries.values)
print("the index of groceries is: ", groceries.index)
print("Is pananas an index label in groceries: ", "bananas" in groceries)
print("Is bread an index label in groceries: ", "bread" in groceries)