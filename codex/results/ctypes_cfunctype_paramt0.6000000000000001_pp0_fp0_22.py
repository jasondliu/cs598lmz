import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# import the module
import py_hann

# create a ctypes function from the python function
f = FUNTYPE(py_hann.pyth_hann)

# and call it
print(f(0.7))

# or get the C-function pointer
cfunc = f.from_address(f.__address__)
print(cfunc(0.7))

# or get the address of the function
print(py_hann.pyth_hann.__address__)

# and call it
cfunc = FUNTYPE(py_hann.pyth_hann.__address__)
print(cfunc(0.7))

# or get the C-function pointer
print(py_hann.pyth_hann.__code__.co_code)
print(ctypes.cast(py_hann.pyth_hann.__code__.co_code, FUNTYPE))
cfunc = ctypes.cast(py_hann.pyth_hann.__
