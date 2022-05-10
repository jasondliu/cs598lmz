import weakref
# Test weakref.ref
class A:
    pass
x = A()
y = weakref.ref(x)
assert y() is x
del x
assert y() is None

# Test weakref.WeakKeyDictionary
class A:
    pass
x = A()
y = A()
d = weakref.WeakKeyDictionary()
d[x] = 1
d[y] = 2
assert d[x] == 1
assert d[y] == 2
del x
assert y in d
del y
assert len(d) == 0

# Test weakref.WeakSet
class A:
    pass
x = A()
y = A()
s = weakref.WeakSet()
s.add(x)
s.add(y)
assert x in s
assert y in s
del x
assert y in s
del y
assert len(s) == 0
