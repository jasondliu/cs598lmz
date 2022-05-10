import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int,ctypes.c_double)
def func(i,x):
    return i*x

func_c = FUNTYPE(func)
print(func_c(1,2))

# function with void return type
FUNTYPE_void = ctypes.CFUNCTYPE(None,ctypes.c_int,ctypes.c_double)
def func_void(i,x):
    print(i*x)

func_c_void = FUNTYPE_void(func_void)
func_c_void(1,2)

# function with pointer
from ctypes import POINTER
def func_pointer(i,x):
    return i*x

func_c_pointer = FUNTYPE(func_pointer)
func_c_pointer_p = POINTER(FUNTYPE)(func_c_pointer)
print(func_c_pointer_p(1,2))

# pointer to pointer
def func_pointer_pointer(i,x):
    return i*x

func_c_pointer_pointer
