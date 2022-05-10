import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int), which
# should return an int.
def callback(x):
    return x*42

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)
c_callback = CMPFUNC(callback)
assert c_callback(6) == 252

# test with callback that accepts a pointer
def ptr_callback(x):
    return x[0]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
c_callback = CMPFUNC(ptr_callback)
buf = ctypes.create_string_buffer(b"abcdefghijkl")
assert c_callback(buf) == ord(b"a")

# test with callback that accepts a string
def str_callback(x):
    return x[:2]

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_
