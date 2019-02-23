import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

df = pd.read_csv('../seds.csv')
AKP = df.loc[(df['msn'] == 'HYTCP') & (df['state_code'] == 'AK')]
AKP = AKP.loc[(AKP['year'] == 2016)]


AKC = df.loc[(df['msn'] == 'HYTCB') & (df['state_code'] == 'AK')]
AKC = AKC.loc[(AKC['year'] == 2016)]
print(AKC['value'])


'''
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
'''