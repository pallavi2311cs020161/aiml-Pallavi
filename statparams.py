#!/usr/bin/env python
# coding: utf-8

# In[3]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter
    return mean 
mean_value(10,20,30,40,50,60)


# In[11]:


def mean_value(L):
    avg = sum(L) / len(L)
    return avg
result = mean_value([3, 5, 9, 10])
print(result)


# In[55]:


def mode_values(s):
    mode=max((s),key=s.count)
    return mode


# In[57]:


mode_values([2,4,4,2,3]) 


# In[112]:


def mode_value(L):
    s = set(L)
    d={}
    for x in s:
         d[x]=L.count(x)
    return(d)


# In[114]:


L = ["M","M","F","M","F","M"]
mode_value(L)


# In[143]:


def mode_value(L):
    s = set(L)
    d={}
    for x in s:
        d[x]=L.count(x)
    m = max(d.values())
    for k in d.keys():
        if d[k] == m:
            return k


# In[145]:


L = ["M","M","F","M","F","M"]
mode_value(L)


# In[147]:


L = [1,1,2,2,3,3,3,4]
mode_value(L)


# In[ ]:




