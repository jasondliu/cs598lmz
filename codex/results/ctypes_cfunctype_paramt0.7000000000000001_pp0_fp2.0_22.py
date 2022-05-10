import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
#FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
def f(x1, x2, x3, x4, x5):
    return 2*x1*x2 + 2*x3*x4 + 2*x4*x5 + 2*x5*x1 + 2*x2*x3 - 2*x1 - 2*x2 - 2*x3 - 2*x4 - x5
    #return 2*x1*x2 + 2*x3*x4 + 2*x2*x3 - 2*x1 - 2*x2 - 2*x3
f_c = FUNTYPE(f)

def g1(x1, x2, x3, x4, x5):
    return x1*x
