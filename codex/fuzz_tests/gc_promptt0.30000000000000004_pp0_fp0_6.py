import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
class A:
    pass

a = A()
r = weakref.ref(a)

gc.collect()
print(gc.garbage)

del a
gc.collect()
print(gc.garbage)
# Test gc.collect() with a weakref to a list
class A:
    pass

a = A()
r = weakref.ref(a)

gc.collect()
print(gc.garbage)

del a
gc.collect()
print(gc.garbage)
# Test gc.collect() with a weakref to a dict
class A:
    pass

a = A()
r = weakref.ref(a)

gc.collect()
print(gc.garbage)

del a
gc.collect()
print(gc.garbage)
# Test gc.collect() with a weakref to a set
class A:
    pass

a = A()
r = weakref.ref(a)

gc.collect()
print(gc.garbage)

del a
gc
