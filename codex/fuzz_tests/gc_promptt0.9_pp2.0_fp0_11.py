import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with cycles and reaching.

import ctypes

class cls:
    pass

def create_cycle():
    if verbose:
        print(gc.collect())

    a = cls()
    weaklist = [weakref.ref(a)]
    a.x = 1
    a.y = a
    if verbose:
        print(gc.collect())

    b = cls()
    b.x = weaklist
    b.y = b
    if verbose:
        print(gc.collect())

    # Create a real reference cycle.
    ctypes.pythonapi.Py_IncRef(ctypes.py_object(b))
    if verbose:
        print(gc.collect())
    return b

def create_homemadecycle(b):
    if verbose:
        print(gc.collect())

    c = cls()
    c.x = b
    b.y = c
    c.y = c
    if verbose:
        print(gc.collect())
    return c

verbose = 0

b1
