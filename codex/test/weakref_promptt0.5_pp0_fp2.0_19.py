import weakref
# Test weakref.ref() on a function.
import pickle

def f(): pass
r = weakref.ref(f)
