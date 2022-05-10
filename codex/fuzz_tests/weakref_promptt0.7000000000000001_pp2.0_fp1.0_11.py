import weakref
# Test weakref.ref with weak-valued dictionaries.

class Foo(object):
    pass

def callback(r):
    global called
    called.append(r)

# Test weakref instances as keys in a weak-valued dictionary.

d = weakref.WeakValueDictionary()
f = Foo()
r = weakref.ref(f, callback)
d[r] = 42
d[f] = 42
del r
del f

called = []
gc.collect()

assert len(called) == 1
assert called[0]() is None

# Test weakref instances as values in a weak-valued dictionary.

d = weakref.WeakValueDictionary()
f = Foo()
r = weakref.ref(f, callback)
d[42] = r
d[42] = f
del r
del f

called = []
gc.collect()

assert len(called) == 1
assert called[0]() is None

# Test weakref instances as both keys and values in a weak-valued dictionary.

d = weakref.WeakValueDictionary()
f
