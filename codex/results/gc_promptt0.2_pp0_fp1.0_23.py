import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

for c in [A, B, C, D, E]:
    a = c()
    a.b = c()
    a.b.a = a
    del a

gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
a.b = b
b.a = a

gc.collect()

r = gc.get_referrers(a)
assert len(r) == 2
assert a in r
assert b in r

r = gc.get_referrers(b)
assert len(r) == 2
assert a in r
assert b in r

r = gc.get_referrers(a, 2)
assert len(r) == 2
assert a in r
assert b in r

r = gc.get_referrers(b
