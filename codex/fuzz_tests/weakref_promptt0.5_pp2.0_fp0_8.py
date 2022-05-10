import weakref
# Test weakref.ref() on a class.
from weakref import ref
from weakref import proxy
from weakref import CallableProxyType
from weakref import ProxyType
from weakref import ReferenceType

class C(object):
    pass

class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

def g():
    pass

def h():
    pass

def i():
    pass

a = C()
b = D()
c = E()
d = F()
e = g
f = h
g = i

# Create some strong references
a.b = b
b.a = a
b.c = c
c.a = a
c.b = b
c.d = d
d.a = a
d.b = b
d.c = c
d.e = e
e.a = a
e.b = b
e.c = c
e.d = d
e.f = f
f.a = a
f.b = b
f.c = c
f.
