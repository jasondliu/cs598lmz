import weakref
# Test weakref.ref
class R(object):
    pass

p = weakref.ref(R())
a = p()
assert isinstance(a, R)
# Test weakref.proxy
class P(object):
    pass

p = weakref.proxy(P())
assert isinstance(p, P)
a = p
# Test weakref.CallableProxyType
import _weakref
WeakCallableProxyType = _weakref.CallableProxyType

class C(object):
    def meth(self):
        pass

def f():
    pass

r = weakref.ref(f)
p = WeakCallableProxyType(r)
assert p() is f
assert callable(p)
assert not isinstance(p, weakref.ProxyType)
c = C()
c.meth()
r = weakref.ref(c.meth)
p = WeakCallableProxyType(r)
assert p() is c.meth
assert callable(p)

# Test weakref.ref subclass support
