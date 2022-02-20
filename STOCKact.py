# import numpy as np
# import pandas as pd

# df = pd.read_csv('SenatorCleaned.csv')

# print(df.head(4))

# # head(#) is top # rows, tail(#) is the bottom

# df.columns #access all column titles

# df['Name'][0:5]  #access the first 5 values of the column 'Name'

# df[['Name', 'Transaction.Date', 'Amount']] #access multiple column values in order of the syntax

# df.iloc[n] #single row data of row 'n'

# df.iloc[1:5] #data from four rows

# df.iloc[2, 5] #access data point using "coordinates"

# for index, row in df.iterrows():
#     print(index, row)               #iterate through all values row by row

# for index, row in df,iterrow():
#     print(index, row["Name"])       #iterate row values within "Name" column

# df.loc[df['Name'] == 'Nancy']       #returns all rows with name "Nancy"

# df.describe() #runs stats on data columns

# df.sort_values('Name') #Sort query by Name in alphabetical order

# df.sort_values('Name', ascending=False)     #Sort alphabetical query with reverse alphabetical logic

# df.sort_values(['Name', 'Amount'], ascending=[1,0]) #Sort 'Name' alphabetically then by Amount descending

# #ADD A TOTAL COLUMN

# df["Total"] = df['']