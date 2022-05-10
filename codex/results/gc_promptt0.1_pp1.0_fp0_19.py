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
    a = c()
    a = None
    gc.collect()
    print gc.collect()

# Test gc.get_referrers()

class A:
    pass

a = A()
l = [a]
d = {'a': a}

print gc.get_referrers(a) == [l, d]

# Test gc.get_referents()

class A:
    pass

a = A()
l = [a]
d = {'a': a}

print gc.get_referents(l) == [a]
print gc.get_referents(d) == [a]

# Test gc.get_objects()

class A:
    pass

a = A()
l = [a]
d = {
