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
assert len(f) == 5
assert a in f and b in f and c in f and d in f and e in f

f = gc.get_referrers(B)
assert len(f) == 2
assert b in f and d in f

f = gc.get_referrers(C)
assert len(f) == 2
assert c in f and d in f

f = gc.get_referrers(D)
assert len(f) == 1
assert
