import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def test():
    # This tests gc.collect() when the finalizer is in a cycle with an object
    # whose tp_del slot is NULL.  This used to crash Python prior to 2.3a1.
    # This test no longer triggers a fatal error (if you compile with
    # Py_TRACE_REFS) because the weakref callbacks can't be called when the
    # garbage collector is running.  But it's a good test to keep around.
    class A:
        pass
    class B:
        pass
    a = A()
    a.b = B()
    a.b.a = a
    a.count = 1
    a.wref = weakref.ref(a, lambda a=a: a.count-=1)
    a.b.count = 1
    a.b.wref = weakref.ref(a.b, lambda b=a.b: b.count-=1)
    del a
    gc.collect()
test()

# Test of the WeakValueDictionary
import operator, sys
class C
