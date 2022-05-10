import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

def g(x):
    return x**3

def h(x):
    return x**4

cf = FUNTYPE(f)
cg = FUNTYPE(g)
ch = FUNTYPE(h)

cf(2)

#%%

import numpy as np
import ctypes

def f(x):
    return x**2

def g(x):
    return x**3

def h(x):
    return x**4

def f_np(x):
    return np.array([f(xi) for xi in x])

def g_np(x):
    return np.array([g(xi) for xi in x])

def h_np(x):
    return np.array([h(xi) for xi in x])

funs = [f, g, h]
funs_np = [f_np, g_np, h_np]

x = np.lins
