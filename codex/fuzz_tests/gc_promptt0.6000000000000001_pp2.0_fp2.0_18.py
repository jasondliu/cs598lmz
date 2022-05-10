import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

# First test if this works at all, by creating a cycle and
# seeing if the callback is called.

class C:
    def __del__(self):
        print "C.__del__"

def callback(wr):
    print "callback:", wr, wr()

c = C()
wr = weakref.ref(c, callback)

# This should trigger the callback
del c
gc.collect()

# Now try the same thing with a cycle.

class D:
    def __init__(self):
        self.c = C()
    def __del__(self):
        print "D.__del__"

d = D()
d.c.d = d

del d
gc.collect()

# Now try the same thing with a cycle and a __del__ method
# in one of the objects.

class E:
    def __init__(self):
        self.c = C()
    def __del__(self):
        print "E.__del__"

e = E()
