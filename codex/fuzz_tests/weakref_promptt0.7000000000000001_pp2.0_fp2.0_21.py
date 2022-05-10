import weakref
# Test weakref.ref
class Object(object):
    pass

# Create a reference
obj = Object()
r = weakref.ref(obj)
assert r() is obj
assert weakref.getweakrefcount(obj) == 1
assert weakref.getweakrefs(obj) == [r]

# Delete a reference
del obj
gc.collect()
assert r() is None

# Test weakref.proxy
obj = Object()
p = weakref.proxy(obj)
assert p is obj
assert weakref.getweakrefcount(obj) == 1
assert weakref.getweakrefs(obj) == [weakref.ref(obj)]

# Delete a reference
del obj
gc.collect()
try:
    p.test
    assert False
except ReferenceError:
    pass

# Test weakref.KeyedRef
class Object(object):
    pass

# Create a reference
obj = Object()
r = weakref.KeyedRef(obj, id(obj))
assert r() is obj
assert weakref.getweakrefcount(obj) == 1
assert weakref.get
