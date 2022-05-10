import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to old style classes

class C:
    pass

def callback(w):
    print("callback:", w)

# Create a cycle, and make sure the objects are collected

c = C()
c.x = c
del c
gc.collect()

# Create a cycle, and make sure the objects are collected

c = C()
c.x = c
w = weakref.ref(c, callback)
del c
gc.collect()

# Create a cycle, and make sure the objects are collected

c = C()
c.x = c
w = weakref.ref(c, callback)
del c
del w
gc.collect()

# Create a cycle, and make sure the objects are collected

c = C()
c.x = c
w = weakref.ref(c, callback)
del c
del w
gc.collect()

# Create a cycle, and make sure the objects are collected

c = C()
c.x = c
w = weakref.ref(c, callback)
c.x = None
