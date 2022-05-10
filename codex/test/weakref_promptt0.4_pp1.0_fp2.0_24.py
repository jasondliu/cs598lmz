import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary()
# Test weakref.WeakValueDictionary()
# Test weakref.WeakSet()
# Test weakref.finalize(obj, callback)

#==============================================================================

# Test weakref.ref(obj)
class C:
    pass
o = C()
r = weakref.ref(o)
assert repr(r) == "<weakref at %#x; to 'C' at %#x>" % (id(r), id(o))
assert r() is o
assert r is not o

# Test weakref.ref(obj, callback)
L = []
def callback(arg):
    L.append(arg)
o = C()
r = weakref.ref(o, callback)
assert r() is o
del o
assert L == [r]

# Test weakref.proxy(obj)
