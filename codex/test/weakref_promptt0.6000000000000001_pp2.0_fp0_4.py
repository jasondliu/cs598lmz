import weakref
# Test weakref.ref()
import _weakref

class C(object):
    def __init__(self, a):
        self.a = a

def f():
    c = C(1)
    r = weakref.ref(c)
    _weakref.ref(c)
    del c
    return r()

f() is None
