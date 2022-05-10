import weakref
# Test weakref.ref()
def f(): pass
r = weakref.ref(f)
assert r() is f
# Test weakref.proxy()
p = weakref.proxy(f)
assert p is f

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
f.attr = 1
d[f] = 2
assert len(d) == 1
del f
assert len(d) == 0

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
f = lambda: None
f.attr = 1
d[1] = f
assert len(d) == 1
del f
assert len(d) == 0

# Test weakref.finalize
obj = object()
finalizer_called = False
def finalizer(arg):
    global finalizer_called
    finalizer_called = True
    assert arg is obj
    assert finalizer.alive
    assert finalizer.detached

finalizer = weakref.finalize(obj, finalizer, obj)
assert finalizer_called == False
del obj
assert
