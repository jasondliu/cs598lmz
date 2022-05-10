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

for o in [A, B, C, D, E]:
    o.attr = o

a = A()
b = B()
c = C()
d = D()
e = E()

w = weakref.ref(a)
del a
gc.collect()
assert w() is None

w = weakref.ref(b)
del b
gc.collect()
assert w() is None

w = weakref.ref(c)
del c
gc.collect()
assert w() is None

w = weakref.ref(d)
del d
gc.collect()
assert w() is None

w = weakref.ref(e)
del e
gc.collect()
assert w() is None

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d =
