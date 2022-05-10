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
    print(c.__name__, gc.get_referents(c))

print(gc.collect())

for c in [A, B, C, D]:
    print(c.__name__, gc.get_referents(c))

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

print(gc.get_referrers(A))
print(gc.get_referrers(B))
print(gc.get_referrers(C))
print(gc.get_referrers(D))

print(gc.get_referrers(a))
print(gc.get_referrers(b))
print(gc.get_referrers(c))
print(gc.get_refer
