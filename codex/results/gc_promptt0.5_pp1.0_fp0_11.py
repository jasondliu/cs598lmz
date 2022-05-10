import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Test gc.collect()
for i in range(10):
    l = [i]
    print(gc.collect())

# Test gc.garbage
gc.garbage[:] = []
l1 = []
l2 = l1
l1.append(l2)
l1 = None
gc.collect()
print(gc.garbage)

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.is_tracked()
print(gc.is_tracked(42))
print(gc.is_tracked(gc.garbage))
print(gc.is_tracked(gc.garbage[0]))

# Test gc.set_threshold()
gc.set_threshold(0)
print(gc.get_threshold())
gc.set_threshold(1, 10, 10)
print(gc.get_threshold())

# Test gc.get_debug()
print(gc.get_debug())

# Test gc.set_debug()

