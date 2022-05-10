import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
def f(x):
    return x**2
f_c = FUNTYPE(f)
f_c(2.)

#%%
from functools import partial
f_c = FUNTYPE(partial(f,2.))
f_c(2.)

#%%
from numba import jit
f_numba = jit(f)
f_numba(2.)

#%%
f_c = FUNTYPE(f_numba)
f_c(2.)

#%%
from scipy.optimize import minimize
res = minimize(f_c,1.)
res

#%%
from scipy.optimize import minimize
res = minimize(f_numba,1.)
res

#%%
from scipy.optimize import minimize
res = minimize(f,1.)
res

#%%
from scipy.integrate import quad
quad(f,0,1)

#%%
from scipy.integrate import quad
quad(f
