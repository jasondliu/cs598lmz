import ctypes
ctypes.cast(a, ctypes.c_void_p).value

#%%
import numpy as np
import ctypes

#%%
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

#%%
c = a*b

#%%
a.ctypes.data_as(ctypes.c_void_p).value

#%%
b.ctypes.data_as(ctypes.c_void_p).value

#%%
c.ctypes.data_as(ctypes.c_void_p).value

#%%
np.may_share_memory(a,b)

#%%
np.may_share_memory(a,c)

#%%
np.may_share_memory(b,c)

#%%
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

#%%
c = np.dot(a,b)

