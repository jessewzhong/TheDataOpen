import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day': [1,2,3,4,5,6], 'Visitors': [43,53,34,45,64,34], 'Bounce_Rate': [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)

#df = df.set_index('Day')
df.set_index('Day', inplace=True) #returns new object
print(df)
print(df['Visitors'])
print(df.Visitors)
print(df[['Bounce_Rate', 'Visitors']])

print(df.Visitors.tolist())
print(df[['Bounce_Rate', 'Visitors']].values.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]).tolist())
'''
print(df.head())
print(df.tail())
print(df.tail(2))
'''