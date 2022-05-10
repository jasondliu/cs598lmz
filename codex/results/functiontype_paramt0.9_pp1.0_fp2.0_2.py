from types import FunctionType
list(FunctionType(func.__code__,globals=globals(),name='func',argdefs=(1,),closure=(a,))())

# ------------------------------------

# In[12]:

def N(n):
    return n + 3

N(5)


# In[13]:

def M(n):
    return n + 4

M(N(5))


# #The power of reducing

# In[14]:

numbers = [1,2,3,4,5,6,7,8,9,10,11]
numbers


# In[15]:

sum(numbers)


# In[16]:

from functools import reduce

reduce(lambda n, n1: n + n1, numbers)


# In[17]:

reduce(lambda x,y: x+y, [0,1,2,3])


# In[18]:

def reducer(function, values):
    value = values[0]
    for item in values[1:]:
        value = function(value
