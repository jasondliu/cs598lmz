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

for o in (a, b, c, d, l, t, d):
    r = gc.get_referrers(o)
    if o is a:
        assert r == [t, d, l]
    elif o is b:
        assert r == [t, d, l]
    elif o is c:
        assert r == [t, d, l]
    elif o
