import weakref
# Test weakref.ref(object)
assert (weakref.ref(object()) is not None)
# Test weakref.ref(object, callback)
def callback(arg):
    pass
assert (weakref.ref(object(), callback) is not None)
# Test weakref.proxy(object)
assert (weakref.proxy(object()) is not None)
# Test weakref.getweakrefcount(object)
assert (weakref.getweakrefcount(object()) == 0)
# Test weakref.getweakrefs(object)
assert (weakref.getweakrefs(object()) == [])
# Test weakref.finalize(object, callback)
def callback(arg):
    pass
assert (weakref.finalize(object(), callback) is not None)
# Test weakref.WeakKeyDictionary()
assert (weakref.WeakKeyDictionary() is not None)
# Test weakref.WeakValueDictionary()
assert (weakref.WeakValueDictionary() is not None)
# Test weakref.WeakSet()
assert (weakref.WeakSet() is not None)

# Test __all
