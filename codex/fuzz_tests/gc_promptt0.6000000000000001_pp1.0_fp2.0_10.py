import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

c = C()
w = weakref.ref(c)
c.attr = 1
del c
gc.collect()
assert w() is None
assert gc.collect() == 0
print "OK"
# Test gc.get_referrers()

a = []
b = [a, a, a]
c = [a, b, a]
del a, b, c

assert gc.get_referrers(1) == [{1: 1}]
assert gc.get_referrers("s") == [{'s': 's'}]
assert gc.get_referrers((1,)) == [(1,)]
assert gc.get_referrers([]) == []
assert gc.get_referrers(object) == [{object: object}]
assert gc.get_referrers(gc) == [{gc: gc}, gc.garbage]

# Test gc.get_referents()

a = []
b = [a, a
