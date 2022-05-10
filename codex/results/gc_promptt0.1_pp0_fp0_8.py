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

a.attr = a
b.attr = b
c.attr = c
d.attr = d

a.attr2 = b
b.attr2 = c
c.attr2 = d
d.attr2 = a

a.attr3 = 1
b.attr3 = 2
c.attr3 = 3
d.attr3 = 4

a.attr4 = [a]
b.attr4 = [b]
c.attr4 = [c]
d.attr4 = [d]

a.attr5 = (a,)
b.attr5 = (b,)
c.attr5 = (c,)
