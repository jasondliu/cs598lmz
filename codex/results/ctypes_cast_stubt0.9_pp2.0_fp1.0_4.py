import ctypes
ctypes.cast(0, ctypes.py_object)

# original
import numpy as np
a = np.zeros(50)
a[:10] = np.nan
a[10:20] = np.nan
a[30] = np.nan

# mask
mask = ~np.isnan(a)

# masked array
a_ma = np.ma.array(a, mask=mask)  # add mask=mask keyword argument

# index ma
index = a_ma.argsort()


# Example:
# use a masked array to find the row/column with
# the most nonzero entries
from numpy import ma
a = ma.array(np.array([[1, 2, 4], [5, 6, 0], [0, 0, 10]]), mask=[[0, 0, 0], [1, 0, 1], [1, 1, 0]])
max_index = np.argmax(np.sum(~a.mask, axis=1))
from numpy import ma
from numpy.random import rand
import sys
from time import time

a
