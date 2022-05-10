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
    gc.garbage = []

# Test gc.get_referents()

a = A()
b = B()
c = C()
d = D()
e = E()

f = [a, b, c, d, e]
g = [f, f, f]

print gc.get_referents(a)
print gc.get_referents(b)
print gc.get_referents(c)
print gc.get_referents(d)
print gc.get_referents(e)
print gc.get_referents(f)
print gc.get_referents(g
