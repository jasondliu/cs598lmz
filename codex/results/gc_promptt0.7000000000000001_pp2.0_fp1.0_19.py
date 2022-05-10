import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a global

class C:
    pass

c = C()
c.a = c

# 'c' has a cyclic reference
r = weakref.ref(c)
gc.collect()
assert r() is c

del c

gc.collect()
assert r() is None

# Test weakref.ref(object, callback)

class C:
    pass

c = C()
c.a = c
count = 0
def callback(x):
    global count
    count += 1

r = weakref.ref(c, callback)

assert count == 0

del c

gc.collect()

assert count == 1
assert r() is None

# Test weakref.ref(object, callback) with an exception

class C:
    pass

c = C()
c.a = c

l = []
def callback(x):
    l.append(x)
    raise SystemError

r = weakref.ref(c, callback)

del c

gc.collect()

assert r() is None

