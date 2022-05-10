import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
class B:
    pass
class C(A, B):
    pass
class D(C, B):
    pass
class E:
    pass
a = A()
b = B()
c = C()
d = D()
e = E()

a.b = b
a.c = c
a.d = d
b.d = d
c.b = b
c.d = d
d.e = e

# Test gc.get_referrers()
def f():
    a = []
    a.append(a)
    return a

def g():
    a = {}
    a[0] = a
    return a

def h():
    a = []
    b = [a, a]
    a.append(b)
    return a

def i():
    a = []
    b = [a, a]
    a.append(a)
    return a

# Test gc.get_referents()
def j():
    a = []
    b
