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

l = [A, B, C, D, a, b, c, d]

# create a reference cycle
a.x = a
b.x = b
c.x = c
d.x = d

# create a reference graph with a cycle
a.y = b
b.y = c
c.y = d
d.y = a

# create a reference graph without a cycle
a.z = b
b.z = c
c.z = d
d.z = None

# create a reference graph with a self-loop
a.w = a
b.w = b
c.w
