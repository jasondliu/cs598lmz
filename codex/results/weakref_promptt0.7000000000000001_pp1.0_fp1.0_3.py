import weakref
# Test weakref.ref(obj)
assert_raises(TypeError, weakref.ref)
assert_raises(TypeError, weakref.ref, 1, 2)

a = []
r = weakref.ref(a)
assert r() is a
assert r is weakref.ref(a)

assert_raises(TypeError, weakref.ref, r, a)

# Test weakref.getweakrefcount(obj)
assert_raises(TypeError, weakref.getweakrefcount)
assert_raises(TypeError, weakref.getweakrefcount, 1, 2)

a = []
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

assert_raises(TypeError, weakref.getweakrefcount, r)

# Test weakref.getweakrefs(obj)
assert_raises(TypeError, weakref.getweakrefs)
assert_raises(TypeError, weakref.getweakrefs, 1, 2)


