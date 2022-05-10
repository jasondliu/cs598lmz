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
    print gc.garbage
    del gc.garbage[:]

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

l = [A, B, C, D, E, a, b, c, d, e]

print gc.get_referrers(A)
print gc.get_referrers(B)
print gc.get_referrers(C)
print gc.get_referrers(D)
print gc.get_referrers(E)
print gc.get_referrers(a)
print gc.get_referrers(
