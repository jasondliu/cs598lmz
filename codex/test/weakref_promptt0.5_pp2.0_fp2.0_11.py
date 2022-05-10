import weakref
# Test weakref.ref() and weakref.proxy()

class C(object):
    pass

o = C()
r = weakref.ref(o)
