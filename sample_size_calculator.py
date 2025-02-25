#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Package
import math


# In[2]:


#Values to provide (Probability, Confidence Interval, Margin of Error)
p = 0.7
z = 1.96
E = 0.05


# In[4]:


#Calculation
n = (p)*(1-p)*(z/E)**2


# In[5]:


#Rounding Off
n_required = math.ceil(n)


# In[6]:


#Final Result
print(f"The sample size required is: {n_required}")


# In[ ]:




