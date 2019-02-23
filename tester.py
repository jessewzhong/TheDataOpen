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

'''
HYTCP
SOTGP
WYTCP
'''

strings = ['HYTCB','SOTCB','WYTCB']

for i in states:
	li = []
	'''
	AKP = df.loc[(df['msn'] in 'HYTCP') & (df['state_code'] == i)]
	AKP = AKP.loc[(1996 <= AKP['year']) & (AKP['year']<= 2016)]
	'''
	dct = {}

	AKC = df.loc[(df['msn'].isin(strings)) & (df['state_code'] == i)]
	AKC = AKC.loc[(1996 <= AKC['year']) & (AKC['year'] <= 2016)]
	for j in strings:
		AKC_temp = AKC.loc[(AKC['msn'] == j)]
		print(AKC_temp)
		temp = AKC_temp['value'].values.tolist()
		dct[j] = temp

	states[i] = dct
	print(pd.DataFrame.from_dict(dct, orient='index'))

	
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