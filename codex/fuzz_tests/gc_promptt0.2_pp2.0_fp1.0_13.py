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

for o in [A, B, C, D, E]:
    o.attr = A()

def f():
    a = A()
    a.b = B()
    a.c = C()
    a.d = D()
    a.e = E()
    return a

a = f()

# Check that a is still alive
assert a.__class__ is A
assert a.b.__class__ is B
assert a.c.__class__ is C
assert a.d.__class__ is D
assert a.e.__class__ is E

# Check that the classes are still alive
assert A.__class__ is type
assert B.__class__ is type
assert C.__class__ is type
assert D.__class__ is type
assert E.__class__ is type

# Check that the class attributes are still alive

