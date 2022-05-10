import weakref
# Test weakref.ref

class C(object):
    pass

c = C()
r = weakref.ref(c)
