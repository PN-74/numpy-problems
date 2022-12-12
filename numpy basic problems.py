#!/usr/bin/env python
# coding: utf-8

# # Create a null vector of size 10 but the fifth value which is 1.

# In[1]:


import numpy as np
     

a= np.zeros(10,dtype='int32')
     

a[4]=1

     

print(a)
     


# # #Create a vector with values ranging from 10 to 49.

# In[4]:


import numpy as np
a = np.arange(10, 50,dtype='int64')
print(a)


# # Create a 3x3 matrix with values ranging from 0 to 8

# In[12]:


import numpy as np
a= np.arange(0, 9,dtype='int32').reshape(3,3)

print(a)


# # 4. Find indices of non-zero elements from [1,2,0,0,4,0]

# In[20]:


import numpy as np
a=np.array([1,2,0,0,4,0])
print("indices of non zeros elements from the array: \n")
for i in range(6) :
 if a[i]!=0 : 
    print(i)
    
    
     


# # Create a 10x10 array with random values and find the minimum and maximum values.

# In[44]:


import numpy as np
arr=np.random.random((10,10))
print("original array:\n",arr)
print("minimum and maximum values of array:\n",arr.min(),arr.max())




# # Create a random vector of size 30 and find the mean value.

# In[59]:


import numpy as np
arr=np.random.random(30)
print(arr)

print('mean value of array:\n')
np.mean(arr)



# In[60]:


np.median(arr)


# In[61]:


np.std(arr)


# In[ ]:




