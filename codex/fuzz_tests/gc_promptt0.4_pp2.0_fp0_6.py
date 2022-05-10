import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
class A:
    pass

def callback(wr, gc_was_enabled):
    print(gc_was_enabled)
    print(wr() is None)

a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()

# Test gc.disable()
gc.disable()
a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()

# Test gc.enable()
gc.enable()
a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()

# Test gc.isenabled()
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
gc.set_threshold(10, 10, 10)
print(gc.get_threshold())

#
