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
    a.x = c
    a.y = c
    a.z = c

del a

# Test gc.collect()

for c in [A, B, C, D]:
    a = c()
    a.x = c
    a.y = c
    a.z = c

del a

# Test gc.collect()

for c in [A, B, C, D]:
    a = c()
    a.x = c
    a.y = c
    a.z = c

del a

# Test gc.collect()

for c in [A, B, C, D]:
    a = c()
    a.x = c
    a.y = c
    a.z = c

del a

# Test gc.
