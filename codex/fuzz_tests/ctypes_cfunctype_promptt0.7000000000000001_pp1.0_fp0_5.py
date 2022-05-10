import ctypes
# Test ctypes.CFUNCTYPE function type

# test a simple function
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f_paramflags = (1, "i", "")
f_restype = ctypes.c_int
f_argtypes = (ctypes.c_int,)

f_ptr = f(lambda i: i + 1).ptr
f_ptr.restype = ctypes.c_int
f_ptr.argtypes = (ctypes.c_int,)
f_ptr.paramflags = (1, "i", "")

assert f_ptr(1) == 2
assert f_ptr(2) == 3
assert f_ptr.paramflags == f_paramflags
assert f_ptr.restype == f_restype
assert f_ptr.argtypes == f_argtypes

assert f(lambda i: i + 1)(2) == 3

# test a function with optional arguments
g = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
