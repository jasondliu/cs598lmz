import weakref
# Test weakref.ref() with an object that has a __del__ method.
import gc
import sys

class C:
    def __init__(self):
        self.x = None
    def __del__(self):
        self.x = None

def f():
    c = C()
    r = weakref.ref(c)
    c.x = r
    del c
    gc.collect()
    return r

r = f()
if r() is not None:
    print("Test failed")
    sys.exit(1)

# Test weakref.ref() with an object that has a __del__ method that
# calls back into Python.

class C:
    def __init__(self):
        self.x = None
    def __del__(self):
        self.x = None

def f():
    c = C()
    r = weakref.ref(c)
    c.x = r
    del c
    gc.collect()
    return r

r = f()
