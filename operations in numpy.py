#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


x = np.arange(10)


# In[5]:


x


# In[36]:


x.sum() #this is for getting the sum in numpy


# In[6]:


y = np.arange(10,20)


# In[7]:


y


# In[8]:


z = x + y


# In[9]:


z


# In[10]:


z = x * y


# In[11]:


z


# In[12]:


z = x - y


# In[14]:


z


# In[15]:


np.sin(x) # this is operation of sin


# In[16]:


np.cos(y) # this is operation of cos


# In[17]:


np.log(y)


# In[18]:


x = np.arange(12).reshape(3,4)


# In[20]:


x


# In[21]:


y = np.arange(10,22).reshape(3,4)


# In[22]:


y


# In[23]:


x + y


# In[27]:


import numpy as np 
a = np.array([0.25, 1.33, 1, 0, 100]) 

print ('Our array is:') 
print (a) 
print ('\n')  

print ('After applying reciprocal function:') 
np.reciprocal(a) 
print ('\n')  

b = np.array([100], dtype = int) 
print ('The second array is:') 
print (b) 
print ('\n')  

print ('After applying reciprocal function:') 
np.reciprocal(b) 


# In[35]:


import numpy as np 
a = np.array([10,100,1000])
b = np.array([1,2,3]) 
np.power(a,b)#This function treats elements in the first input array as base and returns it raised to the power of the corresponding element in the second input array.


# In[30]:


a = np.array([10,100,1000])


# In[31]:


a


# In[32]:


b = np.array([1,2,3]) 


# In[33]:


b


# In[34]:


np.power(a,b)


# In[37]:


import numpy as np 
a = np.array([10,20,30]) 
b = np.array([3,5,7])
np.mod(a,b) #This function returns the remainder of division of the corresponding elements in the input array. The function numpy.remainder() also produces the same result.
np.remainder(a,b) 


# In[40]:


import numpy as np 
a = np.array([-5.6j, 0.2j, 11. , 1+1j])
print(a)
print(np.real(a)) #returns the real part of the complex data type argument
print(np.imag(a)) #returns the imaginary part of the complex data type argument.
print(np.conj(a)) #returns the complex conjugate, which is obtained by changing the sign of the imaginary part.
print(np.angle(a)) #returns the angle of the complex argument. The function has degree parameter. If true, the angle in the degree is returned, otherwise the angle is in radians.
np.angle(a, deg = True)


# In[41]:


arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr.reshape(2,5)


# In[42]:


a = np.array([1,1,2,3,4,5,6])

b = np.array([0,2,1,3,4,8,9])

np.intersect1d(a,b) #How to get the common in between these two arrays


# In[ ]:




