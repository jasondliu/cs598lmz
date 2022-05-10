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
d1 = {'a':a, 'b':b, 'c':c, 'd':d}
d2 = {'A':A, 'B':B, 'C':C, 'D':D}

for o in [a, b, c, d, l, t, d1, d2]:
    r = gc.get_referrers(o)
    assert r[0] is o

# Test gc.get_referents()

for o in [a, b, c,
