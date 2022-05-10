import weakref
# Test weakref.ref()

class C:
    pass

obj = C()
r = weakref.ref(obj)
assert r() is obj

del obj
assert r() is None

# Test weakref.ref(<proxy>)

class C:
    pass

obj = C()
r = weakref.ref(obj)
assert r() is obj

del obj
assert r() is None

# Test weakref.ref(<weak proxy>)

class C:
    pass

obj = C()
r = weakref.ref(obj)
assert r() is obj

del obj
assert r() is None

# Test weakref.proxy()

class C:
    pass

obj = C()
p = weakref.proxy(obj)
assert p is obj

del obj
try:
    p
except ReferenceError:
    pass
else:
    raise Exception("ReferenceError not raised")

# Test weakref.proxy(<proxy>)

class C:
    pass

obj = C()
p = weakref.proxy(obj)
