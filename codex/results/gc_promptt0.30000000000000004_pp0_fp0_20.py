import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    pass

c = C()
c.x = c
c.y = C()
c.y.x = c

w = weakref.ref(c)

gc.collect()

print w() is c
print w() is None

# Test gc.garbage
class C(object):
    pass

c = C()
c.x = c
c.y = C()
c.y.x = c

w = weakref.ref(c)

gc.collect()

print w() is c
print w() is None

# Test gc.get_count()
class C(object):
    pass

c = C()
c.x = c
c.y = C()
c.y.x = c

w = weakref.ref(c)

gc.collect()

print w() is c
print w() is None

# Test gc.get_debug()
class C(object):
    pass

c = C()
c.x = c
c.y
