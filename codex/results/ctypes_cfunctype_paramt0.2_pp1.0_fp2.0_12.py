import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print("myfunc({}, {})".format(a, b))
    return a + b

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(1, 2))

#
#
#

import ctypes

def myfunc(a, b):
    print("myfunc({}, {})".format(a, b))
    return a + b

myfunc_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(myfunc)

print(myfunc_c(1, 2))

#
#
#

import ctypes

def myfunc(a, b):
    print("myfunc({}, {})".format(a, b))
    return a + b

myfunc_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes
