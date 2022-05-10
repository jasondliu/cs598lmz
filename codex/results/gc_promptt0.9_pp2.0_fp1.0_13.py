import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash with combined cyclic tracebacks
class A(object): pass
w = weakref.WeakValueDictionary()
gc.collect()
a = A()
w[1] = a
a.a = a
w[2] = weakref.ref(a)
gc.collect()
print 'ok'
