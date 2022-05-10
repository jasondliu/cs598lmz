import weakref
# Test weakref.ref() on a class instance.

class C(object):
    pass

o = C()
r = weakref.ref(o)

