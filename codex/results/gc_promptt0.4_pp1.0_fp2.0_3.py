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
    a = o()
    wr = weakref.ref(a)
    gc.collect()
    print wr(),
print

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

l0 = [A(), B(), C(), D(), E()]
l1 = [l0, l0, l0]
l2 = [l1, l1, l1]

a.attr = a
b.attr = b
c.attr = c
d.attr = d
e.attr = e

l0[0].attr = l0
l0[1].attr = l0
l0[2].attr = l0
l0[3].attr = l0
l0
