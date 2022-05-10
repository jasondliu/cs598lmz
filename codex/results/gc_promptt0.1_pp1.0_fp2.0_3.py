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
    del a
    gc.collect()
    print gc.garbage

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

f = [a, b, c, d, e]

print gc.get_referrers(a)
print gc.get_referrers(b)
print gc.get_referrers(c)
print gc.get_referrers(d)
print gc.get_referrers(e)

# Test gc.get_referents()

print gc.get_referents(
