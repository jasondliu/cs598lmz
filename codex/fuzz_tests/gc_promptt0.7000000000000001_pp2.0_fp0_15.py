import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect

# Some objects to test collection.
class A:
    pass
class B:
    pass

# A list of all created objects.
all = []
# A list of weakrefs to all created objects.
allwr = []

# Some objects that have a finalizer.
class C:
    def __del__(self):
        print "finalizing C"
all.append(C())

class D:
    def __del__(self):
        print "finalizing D"
all.append(D())

class E:
    def __del__(self):
        print "finalizing E"
all.append(E())

# Some objects that have a weakref finalizer.
class F:
    def __del__(self):
        print "finalizing F"
f = F()
all.append(f)
allwr.append(weakref.ref(f))

class G:
    def __del__(self):
        print "finalizing G"
g = G()
all.append(g)
allwr.append(weakref.ref
