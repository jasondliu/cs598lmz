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

f = gc.get_referrers(A)
assert len(f) == 2
assert A in f
assert type(f[0]) is type
assert type(f[1]) is type

f = gc.get_referrers(B)
assert len(f) == 2
assert B in f
assert type(f[0]) is type
assert type(f[1]) is type

f = gc.get_referrers(C)
assert len(f) == 2
assert C in f
assert type(f[0]) is
