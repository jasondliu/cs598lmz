import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the only weakrefable object holding a reference
# to a collectable object is a weak value dictionary.

class A(object):
   pass

a = A()
w = weakref.WeakValueDictionary()
w[1] = a
del a
gc.collect()
print gc.garbage
# Test gc.collect() when the only weakrefable object holding a reference
# to a collectable object is a weak set.

class A(object):
   pass

a = A()
w = weakref.WeakSet([a])
del a
gc.collect()
print gc.garbage
# Test gc.collect() when the only weakrefable object holding a reference
# to a collectable object is a weak key dictionary.

class A(object):
   pass

a = A()
w = weakref.WeakKeyDictionary()
w[a] = 1
del a
gc.collect()
print gc.garbage
# Test gc.collect() when the only weakrefable object holding a reference
# to a collectable object is a weak method.
