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
    x = c()
    x.foo = x
    x = None
    gc.collect()

# Test gc.get_referrers()

a = A()
a.foo = a

def f():
    a = A()
    a.foo = a
    return a

b = f()

def g():
    a = A()
    a.foo = a
    return lambda : a

h = g()

def h():
    a = A()
    a.foo = a
    return a

i = h()

def j():
    a = A()
    a.foo = a
    return weakref.ref(a)

k = j()

def l():
    a = A()
    a.foo = a
    return weakref.proxy(a)


