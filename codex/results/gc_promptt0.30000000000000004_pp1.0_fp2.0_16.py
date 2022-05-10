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
y = B()
z = C()
w = D()

# Create a reference cycle
x.a = y
y.a = z
z.a = x

# Create a reference cycle
x.b = w
w.b = x

# Create a reference cycle
x.c = w
w.c = y
y.c = x

# Create a reference cycle
x.d = w
w.d = y
y.d = z
z.d = w

# Create a reference cycle
x.e = w
w.e = y
y.e = z
z.e = x

# Create a reference cycle
x.f = w
w.f = y
y.f = z
z.f = w

# Create a reference cycle
x.g = w
w.g = y
y.g = z
z.g = x
