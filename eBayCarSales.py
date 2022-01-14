#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from csv import reader
datadir = os.listdir(".\\datasets")
datafile = open((".\\datasets\\autos.csv"),'r')
print("Contents of the local data directory: ", datadir)
read_file = reader(datafile)
datalist = list(read_file)
datalistheader = datalist[0]
print("\nDatalistHeader\n",datalistheader)
datalistbody = datalist[1:]
print("\nDatalistBody\n",datalistbody[0])


# **This project will reflect ebay sales data and a brief investigation

# In[2]:


import pandas as pd
import numpy as np
autos = pd.read_csv(".\\datasets\\autos.csv")
autos.info()
autos.head()


# The column heads were changed to reflect more accurate information and improve the ability to read the headers

# In[3]:


autos.columns


# In[4]:


autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head()


# In[5]:


autos.describe(include="all")


# In[7]:


autos = autos.drop(["seller", "offer_type"], axis=1)


# In[8]:


autos.describe(include="all")


# In[9]:


autos['num_photos'].value_counts()


# In[10]:


autos = autos.drop(["num_photos"], axis=1)


# In[12]:


autos.describe(include="all")


# In[15]:


autos["price"].head()


# In[18]:


autos["price"] = autos["price"].astype(int)
autos["price"].head()
autos.describe(include="all")


# In[19]:


autos["odometer"].head()


# In[20]:


autos.rename({"odometer":"odometer_km"}, axis=1, inplace=True)
autos["odometer_km"].head()


# In[21]:


autos["odometer_km"].value_counts()


# In[34]:


autos["price"].unique().shape


# In[29]:


autos["price"].describe()


# In[33]:


autos["price"].value_counts().head(20)


# In[38]:


autos["price"].value_counts().sort_index(ascending=False).head(20)


# In[39]:


autos["price"].value_counts().sort_index(ascending=True).head(20)


# In[41]:


autos=autos[autos["price"].between(1,351000)]
autos["price"].describe()


# In[43]:


autos[['date_crawled','ad_created','last_seen']][0:10]


# In[46]:


autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_index()


# In[47]:


autos["date_crawled"].str[:10].value_counts(normalize=True, dropna=False).sort_values()


# In[49]:


autos["last_seen"].str[:10].value_counts(normalize=True, dropna=False).sort_index()


# In[50]:


autos["ad_created"].str[:10].unique().shape
autos["ad_created"].str[:10].value_counts(normalize=True, dropna=False).sort_index()


# In[51]:


autos["registration_year"].describe()


# In[60]:


(autos["registration_year"].between(1900,2016)).sum() / autos.shape[0]


# In[62]:


autos = autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].value_counts(normalize=True).head(20)


# In[63]:


autos["brand"].value_counts(normalize=True)


# In[64]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[65]:


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices


# In[66]:


bmp_series = pd.Series(brand_mean_prices)
pd.DataFrame(bmp_series, columns=["mean_price"])


# In[67]:


brand_mean_mileage = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_mileage = brand_only["odometer_km"].mean()
    brand_mean_mileage[brand] = int(mean_mileage)

mean_mileage = pd.Series(brand_mean_mileage).sort_values(ascending=False)
mean_prices = pd.Series(brand_mean_prices).sort_values(ascending=False)


# In[68]:


brand_info = pd.DataFrame(mean_mileage,columns=['mean_mileage'])
brand_info


# In[69]:


brand_info["mean_price"] = mean_prices
brand_info


# In[ ]:




