import weakref
# Test weakref.ref
import weakref

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f
del f
assert r() is None

# Test weakref.WeakKeyDictionary
import weakref

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1
del f
assert len(d) == 0

# Test weakref.WeakValueDictionary
import weakref

class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d[1] = f
del f
assert len(d) == 0

# Test weakref.WeakSet
import weakref

class Foo:
    pass

f = Foo()
s = weakref.WeakSet()
s.add(f)
del f
assert len(s) == 0

# Test weakref.finalize
import weakref

class Foo:
    pass

f = Foo()
def callback(wr):
    assert wr() is f
   
