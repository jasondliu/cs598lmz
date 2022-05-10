import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
a = np.arange(10)
a

#%%
b = a
b

#%%
np.shares_memory(a, b)

#%%
b[0] = 10
b

#%%
a

#%%
a = np.arange(10)
c = a[::2].copy()  # force a copy
c[0] = 12
a

#%%
c

#%%
np.shares_memory(a, c)

#%%
a = np.arange(10)
a.flags.owndata

#%%
b = a[::2].copy()
b.flags.owndata

#%%
a = np.ones((3, 3))
a.flags.owndata

#%%
b = a.T
b.flags.owndata

#%%
np.shares_memory(a, b)

#%%
b[0, 0] = 2
b

#%%
a
