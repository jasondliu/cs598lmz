import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
b = []
for i in range(10):
    a.append(weakref.ref(a))
    b.append(weakref.ref(b))
del a, b
gc.collect()
gc.collect()
gc.collect()
# Test gc.garbage
a = []
b = []
for i in range(10):
    a.append(weakref.ref(a))
    b.append(weakref.ref(b))
del a, b
gc.collect()
gc.collect()
gc.collect()
print(len(gc.garbage))
# Test gc.get_count()
print(gc.get_count())
# Test gc.get_debug()
print(gc.get_debug())
# Test gc.get_objects()
print(len(gc.get_objects()))
# Test gc.get_referrers()
print(len(gc.get_referrers(gc)))
# Test gc.get_threshold()
print(gc.get_threshold())
# Test g
