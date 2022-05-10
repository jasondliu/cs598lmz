import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

f_c(2)

#%%

import ctypes
import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

f_c([1,2,3])

#%%

import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

f_c([1,2,3])

#%%

import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

f_c([1,2,3])

#%%

import numpy as np

def f(x):
    return x**2

f_c = np.vectorize(f)

f_c([1,2,3])

#%%

import numpy
