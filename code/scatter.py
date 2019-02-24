#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# In[50]:


df = pd.read_csv('power_plants.csv')


# In[49]:


import pandas as pd


# In[106]:


df2 = df.set_index(['primary_source','total_power'])
df3 = df2.iloc[:,:2]
df3.reset_index(level=1, inplace=True)


# In[107]:


hydro = df3.loc['hydroelectric',:]
solar = df3.loc['solar',:]
wind = df3.loc['wind',:]


# In[108]:


h_lat = hydro['latitude'].values
h_long = hydro['longitude'].values
h_pow = hydro['total_power'].values

s_lat = solar['latitude'].values
s_long = solar['longitude'].values
s_pow = solar['total_power'].values

w_lat = wind['latitude'].values
w_long = wind['longitude'].values
w_pow = wind['total_power'].values

xh, yh = m(h_long, h_lat)
xs, ys = m(s_long, s_lat)
xw, yw = m(s_long, s_lat)


# In[101]:


fig = plt.figure(num=None, figsize=(14, 8) ) 
m = Basemap(width=5000000,height=3400000,resolution='c',projection='aea',lat_1=35.,lat_2=40,lon_0=-97,lat_0=39)
m.drawcoastlines(linewidth=0.5)
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.scatter(xh, yh, s = h_pow, alpha = 0.25)
plt.savefig("hydro.png")


# In[109]:


fig = plt.figure(num=None, figsize=(14, 8) ) 
m = Basemap(width=5000000,height=3400000,resolution='c',projection='aea',lat_1=35.,lat_2=40,lon_0=-97,lat_0=39)
m.drawcoastlines(linewidth=0.5)
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.scatter(xs, ys, s = s_pow, color = 'orange', alpha = 0.25)
plt.savefig("solar.png")


# In[110]:


fig = plt.figure(num=None, figsize=(14, 8) ) 
m = Basemap(width=5000000,height=3400000,resolution='c',projection='aea',lat_1=35.,lat_2=40,lon_0=-97,lat_0=39)
m.drawcoastlines(linewidth=0.5)
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
m.drawstates(linewidth=0.5, linestyle='solid', color='k')
m.scatter(xw, yw, color = 'green', s = w_pow, alpha = 0.25)
plt.savefig("wind.png")


# In[ ]:




