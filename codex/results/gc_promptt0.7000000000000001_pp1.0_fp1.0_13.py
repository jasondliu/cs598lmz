import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect to increase the refcount of collectable objects.
# 1) Reference cycles are simply ignored, so they are not collected.
# 2) The collect() call increases the refcount of objects returned by
#    gc.garbage, so they are kept alive.
# 3) Normal objects are also kept alive by the collect() call.
# 4) Python doesn't collect immutable objects, even if they are part of
#    cycles.
l = []
wr = weakref.ref(l)
l.append([l, wr])
del l, wr
gc.collect()
print(len(gc.garbage))
# 2)
print(gc.garbage[1]())
# 3)
print(gc.garbage[0]())
# This should be a reference cycle, so it should not be collected.
print(gc.collect())
print(len(gc.garbage))
# This should be a reference cycle, so it should not be collected.
print(gc.collect())
print(len(gc.garbage))
# This should be a reference cycle, so it should not be collected.
print(gc.
