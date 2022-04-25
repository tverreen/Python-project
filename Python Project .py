#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ###IMPORT DATASET###

# In[24]:


df = pd.read_csv (r"C:\Users\tverr\Documents\python_dataset.zip")


# ###VIEW TOP 5 ROWS OF DATA###

# In[7]:


df.head()


# ###CLEANING THE DATA (CHECKING FOR NAN)###

# In[30]:


pd.isna(pd)


# ###CLEANING THE DATA (DROP UNNECESSARY COLUMNS)###

# In[25]:


to_drop = ['step', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest']
df.drop(to_drop, inplace=True, axis = 1)


# In[11]:


df.head()


# ###CREATING A UNIQUE 'ID' COLUMN TO USE FOR INDEXING###

# In[26]:


df['id'] = np.arange(len(df))


# In[27]:


df.set_index('id', inplace = True)


# In[18]:


df.head()


# ###CHECKING DATA TYPES TO ENSURE THE CODES I WILL RUN WILL WORK###

# In[21]:


df.dtypes


# ### WHAT IS THE MOST HIGH RISK TRANSACTION TYPE? ###

# In[25]:


df.loc[df['isFraud'] == 1].groupby(['type']).count()['isFraud']


# ###ADDING ANOTHER COLUMN TO GIVE INSIGHT ON TRANSACTIONS THAT WERE FRAUD BUT NOT FLAGGED###

# In[28]:


df['Reported'] = df['isFraud']+df['isFlaggedFraud']


# In[29]:


df.head()


# ### WHAT IS THE AVERAGE AMOUNT OF MONEY PER FRAUDULENT TRANSACTION? ###

# In[15]:


means = df.groupby('isFraud')['amount'].mean()
print(means)


# ### HOW MANY TRANSACTIONS WERE FRAUD THAT WERE NOT FLAGGED AS FRAUD ###

# ###0 = NOT FRAUD, 1 = WAS FRAUD BUT NOT FLAGGED, 2 = WAS FRAUD AND WAS FLAGGED###

# In[10]:


df['Reported'].value_counts()


# ###VISUALIZATION OF NON-FLAGGED FRAUD TRANSACTIONS###

# In[51]:


df['Reported'][df['Reported'] > 0].value_counts().plot.pie(figsize = (20,10))

