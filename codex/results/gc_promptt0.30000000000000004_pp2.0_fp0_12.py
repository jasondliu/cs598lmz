import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
b = A()
c = A()

a.b = b
b.a = a

del a, b
gc.collect()

# Test gc.get_referents()
a = A()
b = A()
c = A()

a.b = b
b.a = a

referents = gc.get_referents(a)

assert len(referents) == 2
assert b in referents
assert a in referents

del a, b, c
gc.collect()

# Test gc.get_referrers()
a = A()
b = A()
c = A()

a.b = b
b.a = a

referrers = gc.get_referrers(b)

assert len(referrers) == 2
assert a in referrers
assert b in referrers

del a, b, c
gc.collect()

# Test gc.get_objects()
a = A()

