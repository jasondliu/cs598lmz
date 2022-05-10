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
    a = None
    gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

f = gc.get_referrers(a)
assert len(f) == 1 and f[0] is locals()

f = gc.get_referrers(b)
assert len(f) == 1 and f[0] is locals()

f = gc.get_referrers(c)
assert len(f) == 1 and f[0] is locals()

f = gc.get_referrers(d)
assert len(f) == 1 and f[0] is locals()

f = gc.get_
