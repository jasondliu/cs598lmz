import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# The same code can be used to store arbitrary Python objects in the C
# integer space.

# For example, a doubly linked list can be implemented using only
# integers, with the integer zero used to indicate the end of the list:

def int2addr(i):
    return ctypes.cast(id(i), ctypes.py_object).value

def addr2int(a):
    return ctypes.cast(a, ctypes.py_object).value

