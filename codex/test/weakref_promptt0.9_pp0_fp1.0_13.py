import weakref
# Test weakref.ref for callable objects (only valid for ref objects).
def f():
    pass
r = weakref.ref(f)
