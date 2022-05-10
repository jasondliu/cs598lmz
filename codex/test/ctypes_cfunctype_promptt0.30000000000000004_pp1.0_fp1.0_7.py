import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# define a callback function
def py_callback(x, y):
    print("py_callback called with %d, %d" % (x, y))
    return x + y

# convert the python function to a c function
c_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_callback)

# call the c function
print("c_callback returned %d" % c_callback(1, 2))

# define a callback function
def py_callback(x, y):
    print("py_callback called with %d, %d" % (x, y))
    return x + y

# convert the python function to a c function
c_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_callback)

# call the c function
print("c_callback returned %d" % c_callback(1, 2))

# define a callback function
