import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

import numpy as np

a = np.array([1, 2, 3])
a.shape

b = np.array([[1, 2, 3], [4, 5, 6]])
b.shape

c = np.array([[1], [2], [3]])
c.shape

d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d.shape

e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
e.shape

#%%

import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10
