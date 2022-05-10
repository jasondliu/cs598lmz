import weakref
# Test weakref.ref() and weakref.proxy()

a = [1, 2, 3, 4, 5]
r = weakref.ref(a)
assert r() is a

p = weakref.proxy(a)
assert p[0] == 1
assert p[4] == 5

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()

class Foo(object):
    pass

f = Foo()
d[f] = 1
assert d[f] == 1
del f
gc.collect()
assert len(d) == 0

# Test weakref.WeakValueDictionary()

d = weakref.WeakValueDictionary()

class Foo(object):
    pass

f = Foo()
d[1] = f
assert d[1] is f
del f
gc.collect()
assert len(d) == 0

# Test weakref.WeakSet()

s = weakref.WeakSet()

class Foo(object):
    pass

f = Foo()
s.add(f)
assert f in s
