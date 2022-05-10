import weakref
# Test weakref.ref(obj)

class C(object):
    pass

c = C()
r = weakref.ref(c)
assert r() is c

# Test weakref.ref(obj, callback)

class C(object):
    pass

c = C()
def callback(r):
    assert r() is c
    callback.called = True
callback.called = False
r = weakref.ref(c, callback)
assert not callback.called
del c
assert callback.called

# Test weakref.proxy(obj)

class C(object):
    pass

c = C()
p = weakref.proxy(c)
assert p is c

# Test weakref.proxy(obj, callback)

class C(object):
    pass

c = C()
def callback(r):
    assert r() is c
    callback.called = True
callback.called = False
p = weakref.proxy(c, callback)
assert not callback.called
del c
assert callback.called

# Test weakref.getweakrefcount(obj)


