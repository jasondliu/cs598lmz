import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world!"
fun()

type(ctypes.c_int)
# Add two numbers using ctypes
a = 7
b = 5

libtest = ctypes.CDLL('test')
add = libtest.add
add.argtypes = [ctypes.c_int, ctypes.c_int]
add.restype = ctypes.c_int
add(a, b)

# Calling functions with default argument values
import ctypes
libtest = ctypes.CDLL('./test.so')
libtest.fun()
libtest.fun(1)

# Call a function with variable number of arguements
import sys
import ctypes
args = [int(arg) for arg in sys.argv[1:]]
args.insert(0, len(args))
args = (ctypes.c_int * len(args))(*args)
libtest = ctypes.CDLL('./test.so')
libtest.fun.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

