import weakref
# Test weakref.ref(list)
l = []
r = weakref.ref(l)
assert r() is l

# Test weakref.ref(dict)
d = {}
r = weakref.ref(d)
assert r() is d

# Test weakref.ref(set)
s = set()
r = weakref.ref(s)
assert r() is s

# Test weakref.ref(object)
o = object()
r = weakref.ref(o)
assert r() is o

# Test weakref.ref(int)
i = 123456789
r = weakref.ref(i)
assert r() is i

# Test weakref.ref(float)
f = 12345.6789
r = weakref.ref(f)
assert r() is f

# Test weakref.ref(str)
s = 'hello world'
r = weakref.ref(s)
assert r() is s

# Test weakref.ref(bytes)
b = b'hello world'
r = weakref.ref(b)
assert r() is
