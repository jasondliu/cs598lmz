from types import FunctionType
list(FunctionType(lambda x: x+1, globals())(2), range(10), set(range(8)))

# In[15]:


# generate a list of lists:
# 1. use range() to generate a list of numbers from 0 to 4
# 2. use list comprehension to create a list of lists:
#    ['00', '01', '02', '03']
#    ['10', '11', '12', '13']
#    ['20', '21', '22', '23']
#    ['30', '31', '32', '33']
#   Hint: use str.format()
# 3. write a loop to print out each list on a new line
[[str(i).zfill(2) + str(e).zfill(2) for e in range(4)] for i in range(4)]

# In[16]:


# 1. use range() to generate a list of numbers from 0 to 49
# 2. use list comprehension to create a list of strings:
#    ['01', '02', '03', ..., '49']
# 3. use ','
