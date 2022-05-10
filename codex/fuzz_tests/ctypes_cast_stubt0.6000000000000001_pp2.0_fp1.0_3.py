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

NIL = addr2int(None)

def new(val):
    return [val, NIL, NIL]

def is_empty(l):
    return l is NIL

def value(l):
    return l[0]

def next(l):
    return l[1]

def prev(l):
    return l[2]

def insert(l, x):
    x[1] = l
    if l != NIL:
        x[2] = prev(l)
        prev(l)[1]
