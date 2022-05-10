import weakref
# Test weakref.ref
def f():
    return 42

class C:
    pass

o = C()
r = weakref.ref(o)
