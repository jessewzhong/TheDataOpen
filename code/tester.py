import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


df = pd.read_csv('../seds.csv')

'''
HYTCP
SOTGP
WYTCP
'''

strings_p = ['HYTCP', 'SOTGP', 'WYTCP']
strings_c = ['HYTXB','SOTXB','WYTXB']
names = ['Hydroelectric', 'Solar', 'Wind']

for i in states:
	li = []
	'''
	AKP = df.loc[(df['msn'] in 'HYTCP') & (df['state_code'] == i)]
	AKP = AKP.loc[(1996 <= AKP['year']) & (AKP['year']<= 2016)]
	'''
	dct = {}

	AKP = df.loc[(df['msn'].isin(strings_p)) & (df['state_code'] == i)]
	AKP = AKP.loc[(1996 <= AKP['year']) & (AKP['year'] <= 2016)]

	AKC = df.loc[(df['msn'].isin(strings_c)) & (df['state_code'] == i)]
	AKC = AKC.loc[(1996 <= AKC['year']) & (AKC['year'] <= 2016)]
	for j in range(3):
		AKC_temp = AKC.loc[(AKC['msn'] == strings_c[j])]
		temp_c = AKC_temp['value'].values.tolist()
		temp_c = [k * 0.29307107017 for k in temp_c]

		AKP_temp = AKP.loc[(AKP['msn'] == strings_p[j])]
		temp_p = AKP_temp['value'].values.tolist()

		temp = []
		for k in range(21):
			if temp_c[k] == 0:
				if temp_p[k] != 0:
					temp.append(1)
				else:
					temp.append(0)
			elif temp_p[k] / temp_c[k] > 2:
				temp.append(-1)
			else:
				temp.append(1 - temp_p[k] / temp_c[k])

		dct[names[j]] = temp

	states[i] = dct

	fig = plt.figure()
	ax1 = fig.add_subplot(122, projection='3d')

	major_ticks_y = list(range(1996, 2017, 5))
	major_ticks_x = [1, 1.5, 2, 2.5, 3, 3.5, 4]

	ax1.set_yticks(major_ticks_y)
	ax1.set_xticks(major_ticks_x)
	ax1.set_xticklabels(['', 'Hydroelectric', '', 'Solar', '', 'Wind'])

	xpos = [1]*21 + [2]*21 + [3]*21
	ypos = list(range(1996, 2017, 1)) * 3
	zpos = np.zeros(63)
	dz = dct['Hydroelectric'] + dct['Solar'] + dct['Wind']
	dx = np.ones(63)
	dy = np.ones(63)

	ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=['b'] * 21 + ['orange'] * 21 + ['g'] * 21)
	ax1.set_title(i)
	ax1.set_alpha(0)
	plt.show()

	
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