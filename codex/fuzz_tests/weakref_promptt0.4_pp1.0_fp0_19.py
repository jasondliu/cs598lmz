import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a

a = None
assert r() is None

# Test weakref.WeakKeyDictionary

class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1
assert d[a] == 1

a = None
assert d == {}

# Test weakref.WeakValueDictionary

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d[1] = a
assert d[1] is a

a = None
assert d == {}

# Test weakref.WeakSet

class A:
    pass

a = A()
s = weakref.WeakSet()
s.add(a)
assert a in s

a = None
assert s == set()

# Test weakref.finalize()

class A:
    pass

a = A()

def callback(ref):
    print('callback
