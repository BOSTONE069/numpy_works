#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
x = [[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]] #this is a list of list in numpy
y = np.array(x) # This is for declaring the numpy for the list
y


# In[13]:


import numpy as np
np.zeros((3,3)) -5 #this is a 2D arrays in numpy. This helps in declaring a zero perform operations


# In[11]:


import numpy as np
np.ones((3,4)) # this is a identity matrix involving numpy in ones in 2D


# In[9]:


import numpy as np
np.eye(4) #this is an unity matrix in numpy


# In[14]:


import numpy as np
np.zeros((3,4)) + 5 #this is a 2D arrays in numpy. This helps in declaring a zero perform operations


# In[16]:


import numpy as np
np.arange(10) #This to help in getting arrays using the numpy


# In[20]:


import numpy as np
np.arange(50).reshape(5,10) # this is for getting 50 elements in 5 rows and 10 columns in 2D matrix


# In[23]:


import numpy as np
np.linspace(0,100) # this is for offering linear space between elements


# In[28]:


x = [1,2,3,4,4,8,9,50]
x = np.array(x) 
x.max() # this is for geeting the maximum array in the list provided


# In[27]:


x = [1,2,3,4,4,8,9,50]
x = np.array(x)
x.min() #this is for getting the minimum array in the list provided


# In[31]:


import numpy as np
np.random.rand(10) # this is for getting random values using the numpy


# In[32]:


import numpy as np
np.random.randn(10) # this is for getting random values using the numpy with some in negative


# In[37]:


import numpy as np
np.random.randint(100) # this is for getting random values using the numpy in form of integer


# In[ ]:




