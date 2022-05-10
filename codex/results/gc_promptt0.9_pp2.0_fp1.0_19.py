import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
L = [gc.collect(), gc.collect(), gc.collect()]

# Test gc.set_threshold()
L1 = []
for i in xrange(10):
    L1 = L1 + [gc.collect()]
assert L1 == [1, 1, 1, 2, 2, 2, 3, 3, 1, 1]
gc.set_threshold(700)
L2 = []
for i in xrange(10):
    L2 = L2 + [gc.collect()]
assert L2 == [0, 0, 0, 0, 0, 0, 0, 7, 12, 0]
gc.set_threshold(10)
L3= []
for i in xrange(10):
    L3 = L3 + [gc.collect()]
assert L3 == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Test garbage collection of cycles.
# Create a cycle
c1 = C()
c2 = C()
c1.x = c2
c2.x = c
