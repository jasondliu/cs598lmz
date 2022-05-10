import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

# This is a callback function
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert the Python function into C callback
c_func = CALLBACK(func)

# Call the C function
res = c_func(1, 2)

print("1 + 2 = {0}".format(res))

# Test ctypes.POINTER

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# Create an instance of the Point structure
p = Point(1, 2)

# Create a pointer to the Point instance
ptr = ctypes.pointer(p)

# Access the contents of the pointer
print("The value of the pointer is: {0}".format(ptr.contents))

# Test ctypes.Structure

import ctypes

