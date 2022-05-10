import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = np.arange(4)
xx = np.lib.stride_tricks.as_strided(x,(3,4),(4,4))

#%%
import itertools
a = [[1,2,3],[4,5,6]]
list(itertools.product(*a))

#%%
import random
random.seed(0)
random.random()
random.seed(0)
random.random()

#%%
a = np.arange(10)
a[(0,1,2,3,4)]

#%%
a = np.array([1])
a[0]

#%%
a = np.arange(10)
a[a>5]

#%%
a = np.arange(10)
a[(0,1,2,3,4)]

#%%
a = np.array([[1,2],[3,4]])
a[0,0]
a[0][0]


