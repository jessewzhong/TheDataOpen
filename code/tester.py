import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import states
import matplotlib as mpl

#read from csv file to dataframe
df = pd.read_csv('../../seds.csv')

#empty dictionary to store state abbreviation keys w/ values as dicts
states_stats = {}

#helper lists of codes in seds.csv
strings_p = ['HYTCP', 'SOTGP', 'WYTCP']
strings_c = ['HYTXB','SOTXB','WYTXB']

#axes names
names = ['Hydroelectric', 'Solar', 'Wind']

#gets new dataframe, selecting by code and year
df_codes = df.loc[(df['msn'].isin(strings_p)) | (df['msn'].isin(strings_c))]
df_years = df_codes.loc[(1996 <= df_codes['year']) & (df_codes['year'] <= 2016)]

for i in states.states_dict:
        #empty dict to hold state data
        dct = {}

        #creates dataframes based on state and production/consumption type
        df_state = df_years.loc[(df['state_code'] == i)]
        df_state_p = df_state.loc[(df_state['msn'].isin(strings_p))]
        df_state_c = df_state.loc[(df_state['msn'].isin(strings_c))]

        #loops through each energy type i.e. hydro, solar, wind
        for j in range(3):
                #consumption values
        	df_state_c_temp = df_state_c.loc[(df_state_c['msn'] == strings_c[j])]
        	temp_c = df_state_c_temp['value'].values.tolist()
        	temp_c = [k * 0.29307107017 for k in temp_c] #conversion factor from Btu to KWH

                #production values
        	df_state_p_temp = df_state_p.loc[(df_state_p['msn'] == strings_p[j])]
        	temp_p = df_state_p_temp['value'].values.tolist()

                #list to store 'potential' value based on consumption/production
        	temp = []

                #calculates 'potential' based on data and accounts for edge cases
        	for k in range(21):
        		if temp_c[k] == 0:
        			if temp_p[k] != 0: #production/consumption is infinite, defaults to 1
        				temp.append(-1)
        			else:
        				temp.append(0) #both are 0, defaults to 0
        		elif temp_p[k] / temp_c[k] > 2:
        			temp.append(-1) #defaults to -1 if potential value goes below
        		else:
        			temp.append(1 - temp_p[k] / temp_c[k]) #potential value 

                #sets dict key value of energy type to list of potentials by year              
        	dct[names[j]] = temp

        #sets key of state dict with dict of state data
        states_stats[i] = dct

        #matplotlib plotting 3D bar graph
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')

        major_ticks_y = list(range(1996, 2017, 5))
        major_ticks_x = [1, 1.5, 2, 2.5, 3, 3.5, 4]
        major_ticks_z = [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

        ax1.set_yticks(major_ticks_y)
        ax1.set_xticks(major_ticks_x)
        ax1.set_zticks(major_ticks_z)
        ax1.set_zlim(-1.0, 1.0)
        ax1.set_xticklabels(['', 'Hydroelectric', '', 'Solar', '', 'Wind'])

        xpos = [1]*21 + [2]*21 + [3]*21
        ypos = list(range(1996, 2017, 1)) * 3
        zpos = np.zeros(63)
        dz = dct['Hydroelectric'] + dct['Solar'] + dct['Wind']
        dx = np.ones(63)
        dy = np.ones(63)
        mpl.rcParams['savefig.dpi'] = 1200


        #ax1.tick_params(axis='both', zorder=10000)
        ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=[(0, 0, 1.0, 1)] * 21 + [(1.0, 0.65, 0.0, 1)] * 21 + [(0, 0.5, 0, 1)] * 21)
        ax1.set_title(i)
        ax1.set_alpha(0)
        plt.show()

        	
print(states_stats)