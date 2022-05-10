import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a
a = None
assert r() is None
# Test weakref.ref(x, callback)

class B:
    pass

b = B()
results = []
def callback(wr):
    results.append(wr())

r = weakref.ref(b, callback)
assert r() is b
b = None
assert r() is None
assert results == [None]
# Test weakref.proxy()

class C:
    pass

c = C()
p = weakref.proxy(c)
assert p is c
assert type(p) is weakref.ProxyType
c = None
try:
    p.attr
except ReferenceError:
    pass
