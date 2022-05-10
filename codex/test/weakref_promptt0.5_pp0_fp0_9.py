import weakref
# Test weakref.ref()
class A(object):
    pass
a = A()
assert type(weakref.ref(a)) is weakref.ReferenceType
assert weakref.ref(a)() is a
# Test weakref.proxy()
a = A()
p = weakref.proxy(a)
assert type(p) is weakref.ProxyType
assert p is a
# Test weakref.getweakrefcount()
a = A()
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
p = weakref.proxy(a)
assert weakref.getweakrefcount(a) == 2
# Test weakref.getweakrefs()
a = A()
assert weakref.getweakrefs(a) == [r(), p]
# Test weakref.finalize()
# The finalizer should be called when the referent is garbage-collected
# Note that the finalizer will not be called if the referent is still
# reachable when the interpreter exits.
