import weakref
# Test weakref.ref() with a generator.
import _weakref

class X(object):
    pass

def g():
    for i in (1,2,3):
        yield i

x = X()
x.a = 1
x.b = 2
x.c = 3
x.d = g()
r1 = weakref.ref(x)
r2 = weakref.ref(x.d)
x2 = r2()
assert x is x2
assert x2.a == 1
assert x2.b == 2
assert x2.c == 3
assert iter(x2.d).next() == 1
del x
assert r1() is None
assert r2() is None
