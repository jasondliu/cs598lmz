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

# Test gc.get_referents()

a = A()
b = B()
c = C()
d = D()
e = E()

f = weakref.ref(a)

l = gc.get_referents(a)
assert l == [a], l

l = gc.get_referents(b)
assert l == [b, a], l

l = gc.get_referents(c)
assert l == [c, a], l

l = gc.get_referents(d)
assert l == [d, b, c, a], l

l = gc.get_referents(e)
assert l == [
