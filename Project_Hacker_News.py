#!/usr/bin/env python
# coding: utf-8

# CSV File Setup and Visual Inspection

# In[1]:


import os
from csv import reader
datadir = os.listdir(".\\datasets")
datafile = open((".\\datasets\\hacker_news.csv"),'r',encoding="utf-8")
print("Contents of the local data directory: ", datadir)
read_file = reader(datafile)
datalist = list(read_file)
datalistheader = datalist[0]
print(datalistheader)
datalistbody = datalist[1:]
print(datalistbody[0])


# In[2]:


headers = datalistheader
hn = datalistbody
print(headers)
print(hn[0:5])


# In[3]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    title= title.lower()
 
    if title.startswith("ask hn"):
        ask_posts.append(row)
    elif title.startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))
print("\nAsk Posts\n",ask_posts[0:5])
print("\nShow Posts\n",show_posts[0:5])
print("\nOther Posts\n",other_posts[0:5])


# In[4]:


total_ask_comments = 0
total_show_comments = 0

for row in ask_posts:
    num_comments = int(row[4])
    total_ask_comments = num_comments + total_ask_comments
    
avg_ask_comments = total_ask_comments/len(ask_posts)
print(avg_ask_comments)

for row in show_posts:
    num_comments = int(row[4])
    total_show_comments = num_comments + total_show_comments

avg_show_comments = total_show_comments/len(show_posts)
print(avg_show_comments)


# In[5]:


import datetime as dt
result_list = []

for row in ask_posts:
    created_at = row[6]
    num_comments = int(row[4])
    #Place the values as a single list and append that to result_list
    result_list.append([created_at,num_comments])

counts_by_hour={}
comments_by_hour={}

date_format = "%m/%d/%Y %H:%M"

for row in result_list:
    date = row[0]
    comment = row[1]
    date_time = dt.datetime.strptime(date,date_format)
    time = date_time.strftime("%H")
    
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1
        
print(comments_by_hour)


# In[6]:


avg_by_hour = []

for hr in comments_by_hour:
    #print(comments_by_hour)
    #print(counts_by_hour[hr])
    avg_by_hour.append([hr,comments_by_hour[hr]/counts_by_hour[hr]])



print(avg_by_hour)


# In[7]:


swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1],row[0]])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)
print(sorted_swap)


# In[8]:


print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# In[ ]:




