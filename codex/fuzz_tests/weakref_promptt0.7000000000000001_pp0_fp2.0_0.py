import weakref
# Test weakref.ref(), weakref.proxy() and weakref.getweakrefcount()
import gc

class A:
    pass

def f(x):
    return id(x)

def check(a, b):
    if a != b:
        raise TestFailed, "%s != %s" % (`a`, `b`)


a = A()
check(weakref.getweakrefcount(a), 0)
ra = weakref.ref(a)
del a
gc.collect()
check(ra(), None)
check(weakref.getweakrefcount(ra()), 0)

a = A()
check(weakref.getweakrefcount(a), 0)
ra = weakref.ref(a)
check(weakref.getweakrefcount(a), 1)
rb = weakref.ref(a)
check(weakref.getweakrefcount(a), 2)
del a
gc.collect()
check(weakref.getweakrefcount(ra()), 0)
check(weakref.getweakrefcount(rb()), 0)

a
