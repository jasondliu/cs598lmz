import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()

f = Foo()
d['foo'] = f
assert d['foo'] is f

f = None
assert d['foo'] is None

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()

f = Foo()
d[f] = 'foo'
assert d[f] == 'foo'

f = None
try:
    d[f]
except KeyError:
    pass
else:
    assert False, "expected KeyError"

# Test weakref.WeakSet

s = weakref.WeakSet()

f = Foo()
s.add(f)
assert f in s

f = None
assert f not in s

# Test weakref.finalize()

class Foo:
    pass

f = Foo()

