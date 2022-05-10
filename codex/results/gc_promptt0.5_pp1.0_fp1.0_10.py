import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(C,B):
    pass
class E:
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

print gc.collect()

print gc.get_referrers(A)
print gc.get_referrers(B)
print gc.get_referrers(C)
print gc.get_referrers(D)
print gc.get_referrers(E)

del a, b, c, d, e

print gc.collect()

print gc.get_referrers(A)
print gc.get_referrers(B)
print gc.get_referrers(C)
print gc.get_referrers(D)
print gc.get_referrers(E)

# Test gc.get_objects()
print gc.get_objects()

# Test g
