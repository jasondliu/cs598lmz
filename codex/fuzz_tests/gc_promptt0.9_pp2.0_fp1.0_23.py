import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with some states.
# This is not expected to be very thorough.  The tests in
# test_gc were tested for that.

print 'testing gc.collect()...',
gc.collect()              # Force collection

# SF bug #495324: gc.collect() used to call finalizers even if there
# wasn't an uncollectable object.  This includes a test for that.

class C:
    def __del__(self):
        raise RuntimeError
for i in xrange(5):
    try:
        gc.collect()  # Bug 0.11 did not catch the RuntimeError above
    except RuntimeError:
        pass
C()
gc.collect()

# see bug #18130
class E:
    changed = 0
    def __del__(self):
        self.changed += 1

e = E()
wref = weakref.ref(e)
e2 = wref()
e3 = wref()
gc.collect()
print e.changed

# Testing whether the collector is incremental or not.

try:
    gc
