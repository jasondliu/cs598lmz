import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
