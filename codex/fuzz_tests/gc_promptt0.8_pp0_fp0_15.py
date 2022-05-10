import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

L = []
for i in range(1000):
    L.append(gc.collectable())

for i in range(1000):
    assert gc.collectable(L[i])

assert gc.collectable(42) is False
assert gc.collectable(L) is False
assert gc.collectable(gc) is False

# Test gc.get_referrers()

d = {}

class C(object):
    pass

o = C()
ref = weakref.ref(o)

d[0] = gc.get_referrers(o)
o.attr = o
d[1] = gc.get_referrers(o)
o.attr = 42
d[2] = gc.get_referrers(o)
o.attr = 'xxx'
d[3] = gc.get_referrers(o)
l = [o]
d[4] = gc.get_referrers(o)
del l
d[5] = gc.get_
