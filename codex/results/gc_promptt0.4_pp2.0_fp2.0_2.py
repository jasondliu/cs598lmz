import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect

class A:
    pass

a = A()
w = weakref.ref(a)
del a
gc.collect()
assert w() is None

# Test gc.collect with cyclic garbage

class B:
    pass

b1 = B()
b2 = B()
b1.x = b2
b2.x = b1
b1 = b2 = None
gc.collect()

# Test gc.collect with uncollectable garbage

class C:
    pass

class D:
    pass

c = C()
d = D()
c.x = d
d.x = c
gc.collect()
assert gc.collect() == 0

# Test gc.get_referrers

class E:
    pass

class F:
    pass

e = E()
f = F()
e.x = f
f.x = e

r = gc.get_referrers(e)
assert len(r) == 1 and r[0] is f
r = gc.get_
