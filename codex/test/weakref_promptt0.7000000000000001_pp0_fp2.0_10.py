import weakref
# Test weakref.ref() on functions
def f():
    pass
wr = weakref.ref(f)
