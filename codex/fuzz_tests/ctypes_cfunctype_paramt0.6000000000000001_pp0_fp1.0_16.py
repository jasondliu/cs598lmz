import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_void_p)

def func(x,y):
    print "func called"
    return x**2 + y**2

cfunc = FUNTYPE(func)

print cfunc(1,1)

#print dir(ctypes)
