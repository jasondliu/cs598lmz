import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)
f(2)

#%%
import ctypes
import numpy as np

def func(x):
    return x**2

f = np.frompyfunc(func, 1, 1)
f(2)

#%%
import ctypes
import numpy as np

def func(x):
    return x**2

f = np.vectorize(func)
f(2)

#%%
import numpy as np

def func(x):
    return x**2

f = np.vectorize(func)
f(2)

#%%
import numpy as np

def func(x):
    return x**2

f = np.vectorize(func)
f(2)

#%%
import numpy as np

def func(x):
    return x**2

f = np.vectorize(func)
f(2)

#%%
import
