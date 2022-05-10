import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs.

class C(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "deleting", self.x

wr_c = weakref.ref(C(42))

# we need to create a reference cycle to make sure
# the instance is not immediately collected
a = C(1)
b = C(2)
a.loop = b
b.loop = a

del a, b

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.collect()
print wr_c()

gc.
