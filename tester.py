import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
}


df = pd.read_csv('../seds.csv')

for i in states:
	li = []
	for j in range(1996, 2017, 1):
		AKP = df.loc[(df['msn'] == 'HYTCP') & (df['state_code'] == i)]
		AKP = AKP.loc[(AKP['year'] == j)]

		AKC = df.loc[(df['msn'] == 'HYTCB') & (df['state_code'] == i)]
		AKC = AKC.loc[(AKC['year'] == j)]
		x = AKP.iloc[0]['value']
		li.append(x)

	states[i] = li

	
print(states)





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