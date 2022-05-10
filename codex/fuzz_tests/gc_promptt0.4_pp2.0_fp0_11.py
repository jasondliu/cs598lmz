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

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

assert gc.get_referrers(A) == [{'A': A, 'B': B, 'C': C, 'D': D, 'E': E}]
assert gc.get_referrers(B) == [{'B': B, 'D': D}]
assert gc.get_referrers(C) == [{'C': C, 'D': D}]
assert gc.get_referrers(D) == [{'D': D}]
assert gc.get_referrers(E) ==
