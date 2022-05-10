import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getsizeof(x)

#%%
import numpy as np
x = np.array([1,2,3,4,5])
sys.getsizeof(x)

#%%
x = np.array([1,2,3,4,5], dtype=np.int8)
sys.getsizeof(x)

#%%
x = np.array([1,2,3,4,5], dtype=np.float32)
sys.getsizeof(x)

#%%
x = np.array([1,2,3,4,5], dtype=np.float64)
sys.getsizeof(x)

#%%
x = np.array([1,2,3,4,5], dtype=np.float128)
sys.getsizeof(x)

#%%
x = np.array([1,2,3,4,5], dtype=np.complex64)
sys.getsizeof(x)

