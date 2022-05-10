import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.a = a
    a.c = c
    c.a = a
    return weakref.ref(a), weakref.ref(b), weakref.ref(c)

w1, w2, w3 = f()

# a, b, c are unreachable but not yet collected
gc.collect()

# a, b, c are unreachable and collected
gc.collect()

# a, b, c are gone
w1(), w2(), w3()
