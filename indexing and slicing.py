#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
x = np.arange(0,21)


# In[10]:


x


# In[11]:


x[8] #this is indexing in the numpy


# In[12]:


x[-1] #this is indexing in the numpy


# In[13]:


x[13] #this is indexing in the numpy


# In[14]:


x[:10] #this is slicing in the numpy for getting values from 1 to 10 index


# In[15]:


x[10:] #this is getting the values after the tenth index


# In[16]:


x[2:5]


# In[17]:


x[-10:-1]


# In[20]:


y = x[5:15] =40 # this is for making the the index of 5 to 15 egual to 40 in the list


# In[21]:


y 


# In[22]:


x


# In[23]:


y = x.copy() #this is for copying the modified list into y


# In[24]:


y


# In[25]:


y[5:15] = 80 # this is for modifying the Y list while maitaing the x list


# In[26]:


y


# In[27]:


x


# In[ ]:




