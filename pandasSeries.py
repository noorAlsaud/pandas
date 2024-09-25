import pandas as pd

groceries = pd.Series(data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"])
print(groceries)

# accessing elements with index label: 
print("value in the eggs label is = ", groceries["eggs"])
print(groceries[["milk", "bread"]])
print("---")

# accessing elements by numeric indices: 
print("value in the 1st index = ", groceries[0])
print("value in the last index = ", groceries[-1])
print("values in the series = ", groceries[[0, 1, 3]])

# attribute ( loc ) = location --> explicitly state that I am using Labeled index
print(" try loc : ")
print(groceries.loc[["eggs", "apples"]])

# attribute ( iloc ) = integer location --> explicitly state that I am using numerical index
print(" try iloc : ")
print(groceries.iloc[[2, 3]])

# modify elements in the pandas series : 
groceries ["eggs"] = 2
print(groceries)

# delete elements in the pandas series :
print("series after deleting element")
print(groceries.drop(["apples"]))
# I just noticed that when printing the series, drop() does not reflected !
# If I want to drop elements in the actual series : 
print(groceries.drop(["apples"], inplace=True))
print("*****")
print(groceries) 



