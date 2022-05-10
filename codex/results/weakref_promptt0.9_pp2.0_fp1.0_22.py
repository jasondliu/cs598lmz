import weakref
# Test weakref.ref with proxy objects.
import operator
import gc


class X(object):
    pass


class C(X):
    pass


class Tester(object):

    def __init__(self, obj):
        self.ref = weakref.ref(obj)

    def callback(self, _):
        pass


x = X()
c = C()
r1 = weakref.ref(x, Tester(x).callback)
x = None
c = None
gc.collect()
del r1
gc.collect()
gc.collect()
# Ref does not ref-cycle.
try:
    r2 = weakref.ref(X(), Tester(X()).callback)
except TypeError:
    pass

# callback is a static method.
for cls in [X, C]:
    cls.container = None

    def cb(cls):
        cls.container = []

    cb = staticmethod(cb)
    r = weakref.ref(cls(), cb)
    cls = None
    cb = None
    g
