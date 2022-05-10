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
    a.x = a
    a.y = a
    a.z = a
    a.t = a
    a.u = a
    a.v = a
    a.w = a
    a.s = a

gc.collect()

# Test gc.get_referrers()

a = A()
a.attr = a
a.b = B()
a.b.a = a
a.b.attr = a.b

b = B()
b.attr = b
b.a = a
b.a.b = b
b.a.attr = b.a

a.b = b
b.a = a

gc.collect()

# Test gc.get_referents()

a =
