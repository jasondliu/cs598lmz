import weakref
# Test weakref.ref() on weakly referenced objects, and
# weakref.proxy() on strongly referenced objects.
a = []
p = weakref.proxy(a)
wr = weakref.ref(a)
assert wr() is a
assert p is a
del a
gc.collect()
assert wr() is None
assert p is None
a = []
p = weakref.proxy(a)
wr = weakref.ref(a)
a.append(a)
del a
gc.collect()
assert wr() is None
assert p is None
a = []
p = weakref.proxy(a)
wr = weakref.ref(a)
a.append(wr)
del a
gc.collect()
assert wr() is None
assert p is None
a = []
p = weakref.proxy(a)
wr = weakref.ref(a)
a.append(p)
del a
gc.collect()
assert wr() is None
assert p is None
# Test weakref.ref() on strongly referenced objects, and
# weakref.proxy() on weakly referenced objects.
a = []
