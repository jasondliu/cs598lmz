import weakref
# Test weakref.ref()
import operator


class C(object):
    pass


o = C()
r = weakref.ref(o)
if r() is not o:
    raise RuntimeError
o2 = C()
r2 = weakref.ref(o2)
if r2 is r:
    raise RuntimeError


class D(object):
    pass


d = D()
r = weakref.ref(d)
if r() is not d:
    raise RuntimeError
d2 = D()
r2 = weakref.ref(d2)
if r2 is r:
    raise RuntimeError

# Test weakref.proxy()
p = weakref.proxy(o)
if type(p) is not weakref.ProxyType:
    raise RuntimeError
if p is not o:
    raise RuntimeError
if p.__class__ is not C:
    raise RuntimeError

# Test weakref.getweakrefcount()
if weakref.getweakrefcount(o) != 1:
    raise RuntimeError

# Test weakref.getweakrefs()
