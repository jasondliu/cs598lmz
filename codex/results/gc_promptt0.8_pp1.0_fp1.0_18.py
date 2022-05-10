import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() returns correct count.
gc.collect()

a = weakref.ref(None)
print(gc.collect())

a = weakref.ref(None)
print(gc.collect())

for i in range(100):
    a = weakref.ref(None)
print(gc.collect())

# Weakrefs don't count as cyclic garbage
l = []
a = [l, weakref.ref(None), l]
print(gc.collect())

# If one item in a cyclic garbage group is a weakref,
# the whole group is broken.
import gc
gc.set_debug(gc.DEBUG_LEAK)
a = weakref.ref(None)
b = weakref.ref(None)
l = [a, b, None]
del a, b
print(gc.collect())
print(gc.collect())
print(gc.collect())
#print l

# References to weakrefable objects are tracked
import gc
gc.set_debug(gc.DEBUG_LEAK)
class A: pass
l = []
a
