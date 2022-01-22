#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
vaccinations = pd.read_csv(".\\datasets\\Other_Datasets\\vaccinations.csv")
vaccinations.info()
vaccinations.head()


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
sns.relplot(data=vaccinations, x="date", y="people_vaccinated")
plt.show()


# In[3]:


sns.set_theme()
sns.relplot(data=vaccinations, x="date", y="total_boosters_per_hundred", hue="iso_code", palette='RdYlGn')
plt.show()


# In[5]:


sns.set_theme()
sns.relplot(data=vaccinations, x="date", y="total_boosters_per_hundred", 
            hue="iso_code", palette='RdYlGn', 
            size="total_boosters", sizes=(1,300))
plt.show()


# In[18]:


sns.set_theme()
sns.relplot(data=vaccinations, x="date", y="total_boosters_per_hundred", 
            hue="iso_code", palette='RdYlGn', 
            size="total_boosters", sizes=(1,300), 
           style='people_vaccinated', marker='1')
plt.show()


# In[ ]:


sns.set_theme()
sns.relplot(data=vaccinations, x="date", y="total_boosters_per_hundred", 
            hue="iso_code", palette='RdYlGn', 
            size="total_boosters", sizes=(1,300), 
           style='people_vaccinated', col='location')
plt.show()


# In[ ]:




