import weakref
# Test weakref.ref() without a callable

class C:
    pass

o = C()
r = weakref.ref(o)
