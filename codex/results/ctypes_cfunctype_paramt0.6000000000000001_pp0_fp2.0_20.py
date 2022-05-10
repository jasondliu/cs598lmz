import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

func = FUNTYPE(f)
func(4)

import numpy as np
nx = 1000
x = np.linspace(0,10,nx)
y = func(x)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x,y)

from scipy.optimize import fmin

fmin(func, x0=10)

p = np.polyfit(x,y,4)

plt.plot(x,y)
plt.plot(x,np.polyval(p,x))

np.polyval(p,0)

def f(x):
    return x**2 + 1

func = FUNTYPE(f)

fmin(func, x0=10)

p = np.polyfit(x,y,4)

plt.plot(x,y)
plt.plot(x,np.polyval
