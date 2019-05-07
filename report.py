import pandas as pd

parent = 'parentOrder.xlsx'
child = 'childOrder.xlsx'
fill = 'fillOrder.xlsx'

fileList = [parent, child, fill]

df1 = pd.read_excel(parent)
df2 = pd.read_excel(child)
df3 = pd.read_excel(fill)

print(df1)
print(df2)
print(df3)

v1 = df1[['Order ID', 'Symbol', 'Quantity', 'Side', 'Name', 'Sector']]
v2 = df2[['OrderId', 'ParentOrderId', 'Quantity', 'Broker', 'Price', 'Algo']]
v3 = df3[['FillId', 'ClientOrderId', 'Quantity', 'Price']]

dataframes = [v1, v2, v3]

join = pd.concat(dataframes, sort=False)

join.to_csv("flextradereport.csv")



