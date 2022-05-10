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
    print gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

f = [a, b, c, d, e]
g = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}
h = {g: g}

i = [f, g, h]

print gc.get_referrers(A)
print gc.get_referrers(B)
print gc.get_referrers(C)
print gc.get_referrers(D)
print gc.get_refer
