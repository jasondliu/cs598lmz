import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

for c in [A, B, C, D]:
    print(c.__name__, "refcount", sys.getrefcount(c))

# Create a cycle involving a class
a = A()
a.b = B()
a.c = C()
a.d = D()

# Break the cycle
a = None

# This used to crash
gc.collect()

# Test weakrefs
# Create a cycle involving a class
a = A()
a.b = B()
a.c = C()
a.d = D()

# Create a weak reference to a
w = weakref.ref(a)

# Break the cycle
a = None

# This used to crash
gc.collect()

# Check that the weak reference is dead
try:
    print(w())
except ReferenceError:
    print("weak reference is dead")

