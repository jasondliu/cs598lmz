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

for c in [A, B, C, D]:
    a = c()
    a = None
    gc.collect()
    print gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

l = [A, B, C, D, a, b, c, d, [a], [b], [c], [d]]

gc.collect()

r = gc.get_referrers(A)
r.sort()
assert r == [l, [A]], r

r = gc.get_referrers(B)
r.sort()
assert r == [l, [B]], r

r = gc.get_referrers(C)
r.sort()
assert r == [l, [C]], r

r = g
