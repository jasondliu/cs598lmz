import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#%%
# How to get the current time in Python
import time
time.time()

#%%
# How to convert a list of characters into a string in Python
chars = ['a', 'b', 'c', 'd']
''.join(chars)

#%%
# How to get the number of elements in a list
len(chars)

#%%
# How to check if a string is empty or not in Python
chars = []
not chars

#%%
# How to check if a variable is an integer or not in Python
isinstance(1, int)

#%%
# How to convert a string to an integer in Python
int('1')

#%%
# How to convert a string to a float in Python
float('1.2')

#%%
# How to round a number to a given precision in Python
round(1.23, 1)

#%%
# How to find the type of a variable in Python
type(1)

#%%
# How to get the number of items in
