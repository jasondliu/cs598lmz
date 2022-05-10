import ctypes
# Test ctypes.CFUNCTYPE
#
# This test case demonstrates the use of CFUNCTYPE to create function pointer
# types.

libm = ctypes.CDLL(ctypes.util.find_library("m"))
# try to find sin function
func = libm.sin
fargs = (ctypes.c_double,)
frestype = ctypes.c_double
frestype = ctypes.c_double
# create a ctypes.CFUNCTYPE for the function
cfunc = ctypes.CFUNCTYPE(frestype, *fargs)

# check if the function pointer is callable
try:
    cfunc(func)
except TypeError:
    print("CFUNCTYPE failed")

# test calling the function pointer
print(cfunc(func)(1.0))
print(func(1.0))

# test double free of the function pointer
try:
    del cfunc
except:
    print("double free of CFUNCTYPE failed")

# test more complex function pointer
def func_test(a, b, c):
    return a
