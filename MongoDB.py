#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymongo')
from pymongo import MongoClient
import csv
get_ipython().system('pip install dnspython')



# In[7]:


def get_database():
    from pymongo import MongoClient
    import pymongo
    
CONNECTION_STRING = "mongodb+srv://zakdemir:Ceng476@cluster0.ez5sn.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)


# In[10]:


import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://zakdemir:Ceng476@cluster0.ez5sn.mongodb.net/?retryWrites=true&w=majority")



# In[13]:


from pymongo import MongoClient
client=MongoClient()
  
# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:8888/")
  
# Access database
mydatabase = client['database']
  
# Access collection of the database
mycollection=mydatabase['wine']


# In[17]:


print(mydatabase.wine.count({quality: '5'}))


# In[22]:


from pymongo import MongoClient
client=MongoClient()
client = MongoClient("mongodb://localhost:8888/")

mydatabase = client['database']
print(mydatabase.list_collection_names())


# In[23]:


from pymongo import MongoClient
import pymongo

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://zakdemir:Ceng476@cluster0.ez5sn.mongodb.net/database"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)


# In[24]:


get_ipython().system('pip install dnspython')


# In[ ]:


get_ipython().system('pip install --upgrade pip')


# In[14]:


import pymongo
import pprint
import json
import pprint
import warnings
warnings.filterwarnings('ignore')

client = pymongo.MongoClient("mongodb+srv://zakdemir:Ceng476@cluster0.ez5sn.mongodb.net/?retryWrites=true&w=majority")
dbname = client['database']
mycollection = dbname["wine"]

for i in mycollection.find():
    print(1)


# In[ ]:




