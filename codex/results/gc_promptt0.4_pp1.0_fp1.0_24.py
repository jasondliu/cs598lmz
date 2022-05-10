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

x = A()
w = weakref.ref(x)
x = None
gc.collect()
print(w())

x = B()
w = weakref.ref(x)
x = None
gc.collect()
print(w())

x = C()
w = weakref.ref(x)
x = None
gc.collect()
print(w())

x = D()
w = weakref.ref(x)
x = None
gc.collect()
print(w())

# Test gc.get_referrers()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = A()
w = weakref.ref(x)
x = None
gc.collect()
print(gc.get_referrers(w))

x
