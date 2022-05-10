import weakref
# Test weakref.refs on proxy objects.
import weakref
class Foo(object):
    pass
a = Foo()
r = weakref.ref(a)
print r()

class CustomProxy(object):
    def __init__(self, parent):
        self._parent = parent

    __slots__ = ['_parent']

# Proxy instances store their proxied object in a plain attribute
inst = CustomProxy(42)

# We can create refs to proxy instances as well
wref = weakref.ref(inst)
print wref, wref()

# Check that proxy instances get cleared
a, b = CustomProxy(None), CustomProxy(None)
wref = weakref.ref(a)
print wref, wref()
del a
wref, wref()

a, b = CustomProxy(None), CustomProxy(None)
wref = weakref.ref(a)
print wref, wref()
del b
wref, wref()

class Foo(object):
    pass

a = Foo()
p = CustomProxy(a)
p.__dict
