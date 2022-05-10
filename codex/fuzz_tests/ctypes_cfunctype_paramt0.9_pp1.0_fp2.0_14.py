import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
def foo(x):
    return x*x - 3
cfunc = FUNTYPE(foo)
for i in range(10):
    print("foo({})={}".format(i,cfunc(i)))

##############################################################################

# array to function
import numpy as np
carr = np.array([0.212, -0.87, 0.32, -2.3, 2.87, -0.987])
def myfun(x):
    return carr[x]
c_fun1 = FUNTYPE(myfun)
print("carr={}".format(carr))
for i in range(6):
    print("c_fun1({})={}".format(i,c_fun1(i)))

# function to array
def myfun2(x):
    return x**2
c_fun2 = FUNTYPE(myfun2)
carr2=np.zeros(7)
for i in range(7):
    carr2[i] = myfun2
