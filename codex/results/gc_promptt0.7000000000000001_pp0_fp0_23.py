import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs with callbacks.
class A(object):
    pass
def callback(wr):
    print "CALLBACK", wr
weakrefs = []
for i in range(5):
    a = A()
    weakrefs.append(weakref.ref(a, callback))
    del a
weakrefs.append(weakref.ref(A(), callback))

gc.collect()

weakrefs = []
for i in range(5):
    a = A()
    weakrefs.append(weakref.ref(a, callback))
    del a
weakrefs.append(weakref.ref(A(), callback))

del weakrefs

gc.collect()


# Test gc.collect() on weakrefs with a __del__ method.
class A(object):
    def __del__(self):
        print "DELETED"
weakrefs = []
for i in range(5):
    a = A()
    weakrefs.append(weakref.ref(a))
    del a
weakrefs.append(
