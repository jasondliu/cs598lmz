import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test doesn't check the correctness of gc.collect() but
# only that it doesn't crash.

import gc

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(object):
    pass

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    c.d = d
    d.c = c
    return a

def g():
    a = A()
    b = B()
    c = C()
    d = D()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    c.d = d
    d.c = c
    return d

def h():
    a = A()
    b = B()
    c = C()
    d = D()
    a
