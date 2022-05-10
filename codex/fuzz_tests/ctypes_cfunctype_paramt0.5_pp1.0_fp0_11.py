import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**3

f_c = FUNTYPE(f)

x = np.linspace(-1,1,100)
plt.plot(x, f(x))
plt.plot(x, f_c(x))
</code>

It does not work for functions with more than one argument. I know that it is possible to create a wrapper for functions with more than one argument, but I was wondering if there is an easier way.


A:

You can use <code>np.vectorize</code> to create a vectorized version of your function:
<code>import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

f_c = np.vectorize(f)

x = np.linspace(-1,1,100)
plt.plot(x, f(x))
plt.plot(x, f_c(x))
</code>

