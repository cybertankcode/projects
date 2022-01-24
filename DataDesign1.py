#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sp500 = pd.read_csv(".\\datasets\\Other_Datasets\\sp500_companies\\sp500_index.csv")
sp500.info()
sp500.head()


# In[13]:


sp500.tail()


# In[18]:


date = sp500["Date"]
stocks = sp500["S&P500"]
print(date)
print(stocks)


# In[23]:


plt.plot(date, stocks)
plt.ticklabel_format(axis='y', style="plain")
plt.title("Stocks vs datetime")
plt.xlabel("Datetime")
plt.ylabel("Stocks")
plt.show()


# In[25]:


plt.barh(date,stocks)
plt.title("Stocks vs datetime")
plt.xlabel("Datetime")
plt.ylabel("Stocks")
plt.show()


# In[30]:


fig, ax = plt.subplots()
date = sp500["Date"]
stocks = sp500["S&P500"]
ax.barh(date, stocks)
plt.show()


# In[31]:


fig, ax = plt.subplots(figsize=(4.5,6))
date = sp500["Date"]
stocks = sp500["S&P500"]
ax.barh(date, stocks)
plt.show()


# In[33]:


fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(sp500['Date'],
         sp500['S&P500'])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(bottom=False, left=False)
plt.show()


# In[34]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'])

for location in ['left', 'right', 'bottom', 'top']:
    ax.spines[location].set_visible(False)

plt.show()


# In[36]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.1)

plt.show()


# In[38]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.1)
ax.set_xticks([0,250,500,1000,2000, 4500])

plt.show()


# In[39]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.1)
ax.xaxis.tick_top()
ax.set_xticks([0,250,500,1000,2000, 4500])

plt.show()


# In[40]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.1)
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.set_xticks([0,250,500,1000,2000, 4500])

plt.show()


# In[41]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.1)
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.set_xticks([0,250,500,1000,2000, 4500])

plt.show()


# In[44]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.45, color='#af0b1e')
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='#af0b1e')
ax.set_xticks([0,250,500,1000,2000, 4500])

plt.show()


# In[52]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.45, color='#af0b1e')

for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
    
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.set_xticklabels(['0', '2,000', '3,000'])
ax.text(x=0.5, y=3100,
        s='Dates vs stocks',
        weight='bold', size=17)
ax.text(x=0.5, y=3000.5,
        s='Top 500 Stocks)',
        size=12)
plt.show()


# In[56]:


fig, ax = plt.subplots()
ax.barh(sp500['Date'],
         sp500['S&P500'],
       height=0.45, color='#af0b1e')

for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
    
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.set_xticklabels(['0', '2,000', '3,000'])
ax.text(x=0.5, y=3100,
        s='Dates vs stocks',
        weight='bold', size=17)
ax.text(x=0.5, y=3000.5,
        s='Top 500 Stocks)',
        size=12)

ax.set_yticklabels([]) # an empty list removes the labels
date = sp500['Date']
for i, datetime in zip(range(0,20), date):
    ax.text(x=-1000, y=i-0.15, s=datetime)

ax.axvline(x=2000, ymin=0.045, c='grey', alpha=0.5)

plt.show()


# In[ ]:




