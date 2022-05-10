import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_as_cfunc = FUNTYPE(f)
#f_as_cfunc(2.0)

import numpy as np

x = np.linspace(0, 1, 100)
y = np.zeros_like(x)

for i in range(len(x)):
    y[i] = f_as_cfunc(x[i])

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

#%%
# Passing arrays to C
#
# The ctypes module also allows us to pass arrays to C functions.
#
# To do this, we will need to create a new type, which is a ctypes array type.
#
# The first argument to the array type is the type of the elements in the array.
#
# The second argument is the number of elements in the array.
#
# For example, if we wanted to pass an array of 10 doubles to a
