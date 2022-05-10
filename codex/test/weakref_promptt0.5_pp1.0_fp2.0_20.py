import weakref
# Test weakref.ref(x)
class C(object):
    pass

c = C()
r = weakref.ref(c)
