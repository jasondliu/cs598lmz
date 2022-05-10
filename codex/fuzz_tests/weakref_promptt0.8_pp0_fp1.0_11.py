import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
gc.collect()
assert r() is None
# Test weakref.proxy

class C:
    pass

o = C()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert vars(p) == vars(o)
assert type(p) is type(o)
assert p is o
del o
gc.collect()
try:
    p.attr
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")
# Test weakref.getweakrefcount

class C:
    pass

o = C()
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
del o
assert weakref.getweakrefcount(r) == 1
gc.collect()
assert weakref.getweakrefcount(r) == 0

try:
    weakref.getweakrefcount(1)
except
