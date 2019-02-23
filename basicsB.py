import pandas as pd

df = pd.read_csv('ZILL-Z77006_MLP.csv')
print(df.head())

df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv') #prints to csv

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0) #sets index column
print(df.head())

df.columns = ['Austin_HPI'] #changes column name of other one
print(df.head())

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False) #prints with no headers

df = pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'], index_col=0) #reading from csv with no header
print(df.head())

df.to_html('example.html') #reads to HTMl, SQL, JSON, etc.

df = pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)