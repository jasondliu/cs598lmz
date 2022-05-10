import weakref
# Test weakref.ref()

def f():
    return 42

r = weakref.ref(f)
assert r() == 42

# Test weakref.WeakKeyDictionary

class Foo(object):
    pass

d = weakref.WeakKeyDictionary()
f1 = Foo()
f2 = Foo()

d[f1] = 42
d[f2] = 'hello'

assert d[f1] == 42
assert d[f2] == 'hello'

del f1
assert d[f2] == 'hello'

del f2
try:
    d[f2]
except KeyError:
    pass
else:
    raise Exception, "should have raised KeyError"

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
f1 = Foo()
f2 = Foo()

d[42] = f1
d['hello'] = f2

assert d[42] is f1
assert d['hello'] is f2

del f1
assert d['hello'] is f2

del f
