import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int)
hellofunc = FUNTYPE(lambda x,y: x+y)
hellofunc(1,2)

#%%

from ctypes import *
import ctypes

#(c_double,), (2,), (2,), (c_int, c_int)

def f(x, y):
    return x + y

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int)
f = FUNTYPE(f)
f(1, 2)


#%%

def func(x):
    return x**3 + x**2

dom = np.linspace(0,2,20)



spectrum = np.fft.fft(dom * func(dom))

plt.plot(spectrum)
#%%


def plot_gtp(side):
    
    t = np.linspace(0,2*np.pi,500)
   
