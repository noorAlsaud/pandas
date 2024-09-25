import pandas as pd
import numpy as np

fruits = pd.Series([10, 6, 3], ["apples", "oranges", "bananas"])
# add + 2 in each element in the series : 
print(fruits + 2)

# do numpy operations: 
print(np.sqrt(fruits))