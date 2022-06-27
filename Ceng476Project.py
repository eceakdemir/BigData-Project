#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_csv('winequalityN.csv')


# In[2]:


print(data) 


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[6]:


from mpl_toolkits.mplot3d import Axes3D


# In[7]:


from sklearn.preprocessing import StandardScaler


# In[8]:


nRowsRead = 1000 
df1 = pd.read_csv('winequalityN.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'winequalityN.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')


# In[9]:


data.describe()


# In[21]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import scipy as sp
import os
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler


get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


sns.distplot(data['alcohol'])


# In[24]:


corr = data.corr()
f, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(corr, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, annot=True, mask = mask, cmap=cmap)


# In[37]:


sns.histplot(x='quality', data=data)


# In[38]:


sns.boxplot(x = 'pH', data=data)


# In[ ]:




