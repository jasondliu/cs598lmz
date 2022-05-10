import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
w = weakref.ref(C())

# Test weakref.proxy()
x = weakref.proxy(C())

# Test weakref.getweakrefcount()
weakref.getweakrefcount(C())

# Test weakref.getweakrefs()
weakref.getweakrefs(C())

# Test weakref.finalize()
f = weakref.finalize(C(), lambda: None)
f.detach()

# Test weakref.WeakKeyDictionary()
weakref.WeakKeyDictionary()

# Test weakref.WeakValueDictionary()
weakref.WeakValueDictionary()

# Test weakref.WeakSet()
weakref.WeakSet()
