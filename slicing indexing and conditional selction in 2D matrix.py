#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.arange(25).reshape(5,5)


# In[3]:


x


# In[4]:


x[2,2]


# In[6]:


x[4,2] #this is indexing in numpy


# In[7]:


x[0:2,2:]


# In[8]:


x[1:4,1:4] # this is slicing in the listing


# In[9]:


x[4,2] * 100 # this enables you to perform sum fuctions


# In[11]:


y = np.arange(0,20)


# In[12]:


y


# In[13]:


y[y > 12] # this is conditional selection in the list in y


# In[ ]:




