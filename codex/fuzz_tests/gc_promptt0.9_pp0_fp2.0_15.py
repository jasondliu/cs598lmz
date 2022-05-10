import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect w/weakrefs in containers.

class A:
    pass

# Create some objects, and save a weakref to them
c = A()
d = A()
wref = weakref.ref(d)

# Create some containers, but don't keep any strong references
seen = []
dct = {}

for i in range(10):
    c.x = i
    dct[c] = i
    c.__dict__[i] = i
    d.__dict__[i] = i
    seen.append(d)

for i in range(50):
    gc.collect()

# We'd better not collect d until c is gone
del c
gc.collect()
assert wref() is d

# Ditto for entries in dct and seen...
for i in range(10):
    assert dct[d] == i
    assert seen.pop().__dict__[i] == i

# ...and for any random objects in __dict__ keys
while d.__dict__:
    d.__dict__.popitem()[
