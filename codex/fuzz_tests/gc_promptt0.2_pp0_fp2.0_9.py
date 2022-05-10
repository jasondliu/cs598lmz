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

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    l = [a, b, c, d]
    del a, b, c, d
    return l

def g():
    l = f()
    l = l + l
    return l

def h():
    l = g()
    l = l + l
    return l

def i():
    l = h()
    l = l + l
    return l

def j():
    l = i()
    l = l + l
    return l

def k():
    l = j()
    l = l + l
    return l

def run_test(n):
    print 'Testing with n =', n
    l = k()
    del l
    gc.collect()
    gc.collect()
    gc.
