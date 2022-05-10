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

class F(E):
    pass

class G(E):
    pass

class H(F, G):
    pass

class I(H, D):
    pass

x = I()

print(gc.collect())
print(gc.collect())
print(gc.collect())

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
g = G()
h = H()
i = I()

print(gc.get_referrers(A))
print(gc.get_referrers(B))
print(gc.get_referrers(C))
print(gc.get_referrers(D))
print(gc.get_referrers(E))
print(gc.get_refer
