import weakref
# Test weakref.ref()
def f():
    return 42
o = f
wr = weakref.ref(o)
