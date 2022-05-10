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

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

l = [A, B, C, D]
t = (a, b, c, d)
d = {'a': a, 'b': b, 'c': c, 'd': d}

r = gc.get_referrers(A)
assert r == [l, t, d], r

r = gc.get_referrers(B)
assert r == [l, t, d], r

r = gc.get_referrers(C)
assert r == [l, t, d], r

r = gc.get_referrers(D)
assert r ==
