import weakref
# Test weakref.ref()
def f():
    pass
r = weakref.ref(f)
assert r() is f
# Test weakref.WeakValueDictionary()
class Foo(object):
    pass
f = Foo()
d = weakref.WeakValueDictionary()
d[0] = f
assert len(d) == 1
assert d[0] is f
del f
gc.collect()
assert len(d) == 0
# Test weakref.WeakKeyDictionary()
class Foo(object):
    pass
f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 0
assert len(d) == 1
assert d[f] == 0
del f
gc.collect()
assert len(d) == 0
# Test weakref.WeakSet()
class Foo(object):
    pass
f1 = Foo()
f2 = Foo()
s = weakref.WeakSet()
s.add(f1)
s.add(f2)
assert len(s) == 2
assert f1 in s
assert f2 in s
del f1
gc
