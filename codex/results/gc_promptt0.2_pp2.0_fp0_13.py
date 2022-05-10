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

class A:
    pass

a = A()
b = A()

l = [a]
d = {'a': a}

print gc.get_referrers(a) == [l, d]
print gc.get_referrers(b) == []

# Test gc.get_referents()

class A:
    pass

a = A()
b = A()

l = [a]
d = {'a': a}

print gc.get_referents(l) == [a]
print gc.get_referents(d) == [
