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

values1 = [['Order ID', 'Symbol', 'Quantity', 'Side', 'Name', 'Sector']]
values2 = [['OrderId', 'ParentOrderId', 'Quantity', 'Broker', 'Price', 'Algo']]
values3 = [['FillId', 'ClientOrderId', 'Quantity', 'Price']]

dataframes = [values1, values2, values3]

join = pd.concat(dataframes)

join.to_excel("output.xlsx")



