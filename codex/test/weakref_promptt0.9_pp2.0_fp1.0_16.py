import weakref
# Test weakref.ref
import pickle, copyreg, sys

from weakref import WeakKeyDictionary, WeakValueDictionary, ReferenceType, finalize


def f(o):
    return 42

def g(o):
    return '42'

class Foo(object):
    pass

class MyFoo(Foo):
    pass

class BadFoo(object):
    pass


c1 = int()
c2 = complex()
t1 = f(c1)
t2 = f(c2)

if not (t1 == t2 == 42):
    raise RuntimeError("%r %r" % (t1, t2))

t1 = g(c1)
t2 = g(c2)

if not (t1 == t2 == '42'):
    raise RuntimeError("%r %r" % (t1, t2))


# Same thing, but with copyreg
copyreg.pickle(int, f, g)
c3 = int()
t3 = g(c3)
