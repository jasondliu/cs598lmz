import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass

c = C()
c.a = C()
c.a.b = c

ref = weakref.ref(c)

del c
gc.collect()
assert ref() is None

# Test gc.collect() with a callback
class C:
    pass

c = C()
c.a = C()
c.a.b = c

def callback(obj):
    assert obj is c

ref = weakref.ref(c, callback)

del c
gc.collect()
assert ref() is None

# Test gc.collect() with a callback that creates a reference cycle
class C:
    pass

c = C()
c.a = C()
c.a.b = c

def callback(obj):
    assert obj is c
    obj.a.b = obj

ref = weakref.ref(c, callback)

del c
gc.collect()
assert ref() is None

# Test gc.collect() with a callback that creates a reference cycle
# involving the callback itself

