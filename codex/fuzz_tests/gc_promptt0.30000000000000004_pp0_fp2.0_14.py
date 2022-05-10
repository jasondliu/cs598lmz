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
    b = c()
    a.b = b
    b.a = a
    del a, b

gc.collect()

# Test gc.get_objects()

def f():
    a = A()
    b = B()
    a.b = b
    b.a = a
    del a, b

f()
gc.collect()

# Test gc.get_referrers()

def f():
    a = A()
    b = B()
    a.b = b
    b.a = a
    del a, b

f()
gc.collect()

# Test gc.get_referents()

def f():
    a = A()
    b = B()
    a.b = b
    b.a = a
   
