import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer to a function taking a float, returning an int
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)(
        ('testfunc_f_i', lib), ((1,),))

print f(2.0)

# a function pointer to a function taking a float, returning a float
f = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)(
        ('testfunc_f_f', lib), ((1,),))

print f(2.0)

# a function pointer to a function taking an int, returning a float
f = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_int)(
        ('testfunc_i_f', lib), ((1,),))

print f(2)

# a function pointer to a function taking an int, returning a void
f = ctypes.CFUNCTY
