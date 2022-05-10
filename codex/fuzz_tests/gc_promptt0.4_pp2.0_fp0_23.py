import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
ref = weakref.ref(object())

# Test weakref.proxy()
proxy = weakref.proxy(object())

# Test weakref.getweakrefcount()
weakref.getweakrefcount(object())

# Test weakref.getweakrefs()
weakref.getweakrefs(object())

# Test weakref.WeakKeyDictionary()
weakref.WeakKeyDictionary()

# Test weakref.WeakValueDictionary()
weakref.WeakValueDictionary()
