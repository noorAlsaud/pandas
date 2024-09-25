import pandas as pd

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

shopping_carts = pd.DataFrame(items)

print(shopping_carts)
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)

# one data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])
print("Bob Cart: ", bob_shopping_cart)

# DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# display sel_shopping_cart
print(sel_shopping_cart)
print("---")
# DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# display alice_sel_shopping_cart
print(alice_sel_shopping_cart)
print("---")

# dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# create a DataFrame 
df = pd.DataFrame(data)

# display the DataFrame
print(df)
print("---------")
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}
DF = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

# display the DataFrame
print(DF)
print("---------")
