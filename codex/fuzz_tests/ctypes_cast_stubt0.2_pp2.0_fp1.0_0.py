import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getsizeof(x)

#%%
x = np.random.randint(0, 100, size=(100, 100))

#%%
x.nbytes

#%%
x.itemsize

#%%
x.dtype

#%%
x.dtype.name

#%%
x.dtype.itemsize

#%%
x.dtype.alignment

#%%
x.dtype.str

#%%
x.dtype.str.split('|')

#%%
x.dtype.str.split('|')[0]

#%%
x.dtype.str.split('|')[1]

#%%
x.dtype.str.split('|')[2]

#%%
x.dtype.str.split('|')[3]

#%%
x.dtype.str.split('|')[4]

#%%
x.dtype.str.split('|')[5]
