import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getsizeof(x)

#%%
x = np.ones(10)
sys.getsizeof(x)

#%%
x = np.ones(1000)
sys.getsizeof(x)

#%%
x = np.ones(1000000)
sys.getsizeof(x)

#%%
x = np.ones(100000000)
sys.getsizeof(x)

#%%
x = np.ones(1000000000)
sys.getsizeof(x)

#%%
x = np.ones(10000000000)
sys.getsizeof(x)

#%%
x = np.ones(100000000000)
sys.getsizeof(x)

#%%
x = np.ones(1000000000000)
sys.getsizeof(x)

#%%
x = np.ones(10000000000000)
sys.getsizeof(x)

#%%
x = np.ones(100000000000000)
sys
