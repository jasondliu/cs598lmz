import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)

