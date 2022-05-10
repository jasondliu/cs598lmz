import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

import sys
sys.getsizeof(x)

#%%

x = [1,2,3,4,5,6,7,8,9,10]
y = x

#%%

x = [1,2,3,4,5,6,7,8,9,10]
y = x

y[0] = 100

#%%

x = [1,2,3,4,5,6,7,8,9,10]
y = x

y = [100,200,300]

#%%

x = [1,2,3,4,5,6,7,8,9,10]
y = x

y = [100,200,300]

print(x)

#%%

x = [1,2,3,4,5,6,7,8,9,10]
y = x

y = [100,200,300]

print(x)

print(y)


