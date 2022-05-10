import weakref
# Test weakref.ref() with a class instance.

class C(object):
    pass

o = C()
r = weakref.ref(o)
