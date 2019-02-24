import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import states

df = pd.read_csv('../../seds.csv')

states_stats = {}

strings_p = ['HYTCP', 'SOTGP', 'WYTCP']
strings_c = ['HYTXB','SOTXB','WYTXB']
names = ['Hydroelectric', 'Solar', 'Wind']

df_codes = df.loc[(df['msn'].isin(strings_p)) | (df['msn'].isin(strings_c))]
df_years = df_codes.loc[(1996 <= df_codes['year']) & (df_codes['year'] <= 2016)]

for i in states.states_dict:
	dct = {}

	df_state = df_years.loc[(df['state_code'] == i)]
	df_state_p = df_state.loc[(df_state['msn'].isin(strings_p))]
	df_state_c = df_state.loc[(df_state['msn'].isin(strings_c))]

	for j in range(3):
		df_state_c_temp = df_state_c.loc[(df_state_c['msn'] == strings_c[j])]
		temp_c = df_state_c_temp['value'].values.tolist()
		temp_c = [k * 0.29307107017 for k in temp_c]

		df_state_p_temp = df_state_p.loc[(df_state_p['msn'] == strings_p[j])]
		temp_p = df_state_p_temp['value'].values.tolist()

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

	states_stats[i] = dct

	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')

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

	
print(states_stats)