import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
a.append(a)
b = []
b.append(b)
a.append(b)
b.append(a)
del a, b
gc.collect()
# Test gc.is_tracked()
a = []
a.append(a)
b = []
b.append(b)
a.append(b)
b.append(a)
assert gc.is_tracked(a)
assert gc.is_tracked(b)
del a, b
gc.collect()
assert not gc.is_tracked(a)
assert not gc.is_tracked(b)
# Test gc.get_referents()
a = []
a.append(a)
b = []
b.append(b)
a.append(b)
b.append(a)
assert gc.get_referents(a) == [a, b]
assert gc.get_referents(b) == [b, a]
del a, b
gc.collect()
assert not gc
