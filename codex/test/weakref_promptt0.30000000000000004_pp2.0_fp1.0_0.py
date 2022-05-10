import weakref
# Test weakref.ref() on a class instance.

class C(object):
    pass

c = C()
r = weakref.ref(c)
