import gc, weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
