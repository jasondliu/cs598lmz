import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)

a = []
b = a
del a
print(gc.collect())
print(gc.garbage)

# gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# Test weakref
class A:
    pass
a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
print(gc.collect())
print(d['primary'])
