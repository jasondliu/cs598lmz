import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
gc.collect()

# Test weakref.proxy()
p = weakref.proxy(f)
gc.collect()

# Test weakref.getweakrefcount()
gc.collect()

# Test weakref.getweakrefs()
gc.collect()

# Test weakref.finalize()
gc.collect()

# Test weakref.WeakKeyDictionary()
gc.collect()

# Test weakref.WeakValueDictionary()
gc.collect()

# Test weakref.WeakSet()
gc.collect()

# Test weakref.finalize()
gc.collect()

# Test weakref.WeakMethod()
gc.collect()

# Test weakref.WeakMethod()
gc.collect()

# Test weakref.finalize()
gc.collect()

# Test weakref.finalize()
gc.collect()

# Test weakref.finalize()
gc.collect()
