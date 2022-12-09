#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


police= pd.read_csv(r'C:\Users\Hp\Desktop\Python Project\Police_data\Police_Data.csv')


# In[4]:


police.head(2)


# In[ ]:


#Remove the coloum that only contain Missing values


# In[7]:


police.isnull().sum()


# In[12]:


police.drop(columns ='country_name', inplace = True)


# In[13]:


police


# In[ ]:


Based on Filtering and Value counts
for Speeding , were men or women stopped more often


# In[14]:


police[police.violation == 'Speeding'].driver_gender.value_counts()


# In[ ]:


#group by 
get_ipython().set_next_input('Does gender affect who gets searched during a stop');get_ipython().run_line_magic('pinfo', 'stop')


# In[16]:


police.head(2)


# In[17]:


police.groupby('driver_gender').search_conducted.sum()


# In[ ]:


get_ipython().set_next_input('How many time searched was conducting');get_ipython().run_line_magic('pinfo', 'conducting')


# In[20]:


police.search_conducted.value_counts()


# In[ ]:


Mapping and Type_casting 
get_ipython().set_next_input('What is the mean stop_duration');get_ipython().run_line_magic('pinfo', 'stop_duration')


# In[21]:


police.head(2)


# In[22]:


police.stop_duration.value_counts()


# In[26]:


police['stop_duration'] = police['stop_duration'].map({'0-15 Min' : 7.5, '16-30 Min': 24, '30+ Min': 45})


# In[28]:


police['stop_duration'].mean()


# In[ ]:


Groupby and Describe
Compare the age distribution for each violations


# In[29]:


police.head(2)


# In[33]:


police.groupby('violation').driver_age.describe()


# In[ ]:




