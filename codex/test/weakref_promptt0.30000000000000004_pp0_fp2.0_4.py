import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None

# Test weakref.proxy

o = C()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert p.__weakref__ is not None
assert p.__dict__ is o.__dict__
assert p.__doc__ is o.__doc__
assert p.__module__ is o.__module__
assert p.__weakref__ is o.__weakref__
assert p.__dict__ is o.__dict__
assert p.__doc__ is o.__doc__
assert p.__module__ is o.__module__

# Test that the proxy is usable

p.x = 1
assert p.x == 1
assert o.x == 1

# Test that the proxy is weak

del o
try:
    p.x
except ReferenceError:
    pass
