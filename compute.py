#!/usr/bin/env python
# coding: utf-8

# In[1]:


#compute a mean value


# In[3]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter
    return mean 


# In[5]:


#find the product of given numbers


# In[5]:


def product (*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[7]:


product(1,2,3,4)


# In[ ]:




