import ctypes
# Test ctypes.CFUNCTYPE()
def add(a, b):
    return a + b

my_add = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(add)
my_add(2, 3)

def add(a, b):
    return a + b

# create ctypes for all arguments and return type
add_ctypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
# create functools.partial object with first argument fixed to 2
partial = functools.partial(add_ctypes(2), b=3)
# call it - 2 + 3 = 5
partial()

# similarly
add_ctypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
partial = functools.partial(add_ctypes, 2, b=3)
partial()
 
def add(a, b):
    return a + b

add
