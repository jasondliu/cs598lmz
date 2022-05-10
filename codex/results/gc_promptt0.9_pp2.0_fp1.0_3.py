import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
b = A()
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
del b
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
del A.begin, A.end
gc.collect()
print [weakref.ref(c) for c in gc.get_objects()
#if isinstance(c, A)]
del A.m
gc.collect()
print [weakref.ref(c) for c in gc.get
