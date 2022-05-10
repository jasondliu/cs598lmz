import weakref
# Test weakref.ref() on a function.
import gc

def f():
    pass

r = weakref.ref(f)
