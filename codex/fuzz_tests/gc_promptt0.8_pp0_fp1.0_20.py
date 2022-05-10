import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.
class A:
    l = weakref.WeakKeyDictionary()
    def __del__(self):
        print "A's __del__ called"

def f():
    a = A()
    A.l[a] = 1
    print weakref.getweakrefcount(a)
    del a
    gc.collect()
    print weakref.getweakrefcount(A.l)

def g():
    f()
    print weakref.getweakrefcount(A.l)
    print len(A.l)

g()
