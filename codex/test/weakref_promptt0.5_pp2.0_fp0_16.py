import weakref
# Test weakref.ref() with an object that does not have a __dict__
# and does not support weak references.
class C:
    pass

x = C()
r = weakref.ref(x)
