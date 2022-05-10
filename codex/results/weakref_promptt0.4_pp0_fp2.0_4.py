import weakref
# Test weakref.ref() and weakref.proxy()

# Test basic weakref.ref()
class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None

# Test weakref.ref() with a callback
class C:
    pass

o = C()
l = []
def callback(arg):
    l.append(arg)

r = weakref.ref(o, callback)
assert r() is o
del o
assert r() is None
assert l == [o]

# Test basic weakref.proxy()
class C:
    pass

o = C()
p = weakref.proxy(o)
assert p is o
del o
try:
    p.foo
except ReferenceError:
    pass
else:
    assert False, "expected ReferenceError"

# Test weakref.proxy() with a callback
class C:
    pass

o = C()
l = []
def callback(arg):
    l.append(arg)

p = weakref.proxy(
