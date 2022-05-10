import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()



# Provides test for bug #376959
def on_finalize(ref):
    print "finalizer executed"
    # Now the bug occurs... If a cycle of collectable objects,
    # with a common __del__ method, is not correctly collected,
    # this function may be called more than once.
class Foo:
    def __del__(self):
        self.stop()
    def stop(self):
        print "stopping"
        del self.loop
f1 = Foo()
f2 = Foo()
f1.loop = f2
f2.loop = f1
# Create cycle of collectable objects
del f1.loop
del f2.loop
# Create a weak reference pointing to the last living instance of 'Foo'
ref = weakref.ref(f1)
ref_id = id(ref)
wr = weakref.ref(f2)
# Create a finalize pointing to the last living instance of 'Foo'
wr.finalize(on_finalize)
f1 = f2 = wr = ref = None

