import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() re-schedules dead weakref.
#
refs = []
for i in xrange(1000):
    o = gc.collect()
    refs.append(weakref.ref(object()))
#
import time
for i in xrange(10):
    time.sleep(1.0)
    print gc.collect()
