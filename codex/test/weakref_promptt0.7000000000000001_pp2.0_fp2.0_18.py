import weakref
# Test weakref.ref() and weakref.proxy(obj)
import gc

class C:
    pass

o = C()

r = weakref.ref(o)
assert r() is o
assert r() is not None
assert r() is r()

p = weakref.proxy(o)
assert p is o
assert p is not None
assert p is p

assert not hasattr(p, '__weakref__')
assert hasattr(o, '__weakref__')
assert r().__weakref__() is r

# Test invaild objects
try:
    weakref.ref(100)
except TypeError as e:
    assert str(e) == "cannot create weak reference to 'int' object"

try:
    weakref.proxy(100)
except TypeError as e:
    assert str(e) == "cannot create weak reference to 'int' object"

# Test callback
l = []
def callback(obj):
    l.append(obj)

wr = weakref.ref(o, callback)
