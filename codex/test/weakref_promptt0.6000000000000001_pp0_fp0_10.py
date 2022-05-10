import weakref
# Test weakref.ref(obj)

# Test weakref.ref(obj, callback)

# Test weakref.proxy(obj)

# Test weakref.proxy(obj, callback)

# Test weakref.getweakrefcount(obj)

# Test weakref.getweakrefs(obj)

# Test weakref.WeakKeyDictionary(dict)

# Test weakref.WeakValueDictionary(dict)


# Test weakref.WeakSet(iterable)

class A:
    pass

a = A()

# Test weakref.WeakSet(iterable)

w = weakref.WeakSet(range(10))
assert len(w) == 10
assert 0 in w
assert 11 not in w
w.add(a)
assert len(w) == 11
assert a in w
del a
assert len(w) == 10
assert a not in w


# Test weakref.WeakSet.add(item)

w = weakref.WeakSet()
assert len(w) == 0
w.add(a)
assert len(w) == 1
