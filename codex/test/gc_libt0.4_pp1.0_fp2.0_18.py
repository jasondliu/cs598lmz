import gc, weakref

class C(object):
    pass

c = C()

w = weakref.ref(c)

