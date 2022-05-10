import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
print 'gc.collect()'
gc.collect()

# Test weakref.ref
print 'weakref.ref'
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print r()
del f
gc.collect()
print r()

# Test weakref.proxy
print 'weakref.proxy'
class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
print p
del f
gc.collect()
print p

# Test weakref.WeakKeyDictionary
print 'weakref.WeakKeyDictionary'
class Foo:
    pass

d = weakref.WeakKeyDictionary()
f = Foo()
d[f] = 1
del f
gc.collect()
print d

# Test weakref.WeakValueDictionary
print 'weakref.WeakValueDictionary'
class Foo:
    pass

d = weakref.WeakValueDictionary()
f = Foo()
d[1] = f
del f
gc.collect()
print d

# Test weakref
