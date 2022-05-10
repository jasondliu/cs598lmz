import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

#defining functions

def func1(x):
    return x*x

def func2(x):
    return x*x + 2*x + 1

def func3(x):
    return x**3 + 2*x*x + 2*x + 1

#defining the functions as ctypes
cfunc1 = FUNTYPE(func1)
cfunc2 = FUNTYPE(func2)
cfunc3 = FUNTYPE(func3)

#defining the functions as array to use in library
funcs = (cfunc1,cfunc2,cfunc3)

#defining the library
mylib = ctypes.CDLL("/mnt/d/Coding/C++/Iterative Methods/Python/library.so")

#defining the function pointer array
array_type = cfunc1 * 3
func_array = array_type(*funcs)

#defining the parameters
p = ctypes.c_double(0.5)
tol = ctypes.c_double(
