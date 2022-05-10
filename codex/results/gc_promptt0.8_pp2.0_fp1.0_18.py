import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.
# Starts with a large number of noncollectable objects so
# that we don't have to disable collection in individual
# tests.
a = []
for i in range(101):
    a.append(str(i) * 10000)
b = []
for i in range(101):
    b.append(i * "abc")
a = None
print(len(gc.garbage))
assert len(gc.garbage) >= 202
print(gc.collect())
assert len(gc.garbage) == 0
print("Done.")

# Test gc.get_count.
a = []
a.append(a)
gc.collect()
print(gc.get_count())
del a
assert gc.collect() == 1
print(gc.get_count())

# Test gc.get_objects.
a = []
a.append(a)
gc.collect()
assert gc.get_objects()
del a
assert not gc.get_objects()
assert gc.collect() == 1
assert not gc.get_objects()

# Test
