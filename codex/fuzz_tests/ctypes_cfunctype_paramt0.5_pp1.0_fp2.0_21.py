import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@FUNTYPE
def add_one(x):
    return x + 1

add_one(1)

def add_one(x):
    return x + 1

add_one.__code__ = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(add_one.__code__)

add_one(1)
</code>
This works because the first argument to <code>CFUNCTYPE</code> is a list of types, and the second argument is the Python function object.

