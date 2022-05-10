import weakref
# Test weakref.ref() on a function object.
def f():
    pass
r = weakref.ref(f)
