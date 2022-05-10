import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Global
def f():
    return

class A:
    def __del__(self):
        pass

    def f(self):
        return

a = A()
a1 = A()
a2 = A()
a1.f = f
a2.f = a.f
del a
del a1
del a2
# Local
def g():
    def f():
        return
    a = A()
    a1 = A()
    a2 = A()
    a1.f = f
    a2.f = a.f
    del a
    del a1
    del a2

g()
# Weakref
def h():
    def f():
        return
    a = A()
    a1 = A()
    a2 = A()
    a1.f = f
    a2.f = a.f
    w = weakref.ref(a)
    w1 = weakref.ref(a1)
    w2 = weakref.ref(a2)

h()
gc.collect()

