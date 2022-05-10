import weakref
# Test weakref.ref

class C(object):
    pass

o = C()
r = weakref.ref(o)

