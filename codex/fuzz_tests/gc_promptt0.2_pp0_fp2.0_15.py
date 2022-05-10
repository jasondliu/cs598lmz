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

#print gc.get_referrers(A)
#print gc.get_referrers(B)
#print gc.get_referrers(C)
#print gc.get_referrers(D)

#print gc.get_referrers(a)
#print gc.get_referrers(b)
#print gc.get_referrers(c)
#print gc.get_referrers(d)

#print gc.get_
