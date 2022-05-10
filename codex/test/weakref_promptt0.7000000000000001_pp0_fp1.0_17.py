import weakref
# Test weakref.ref on a class.
class C:
    pass

o = C()
r = weakref.ref(o)
