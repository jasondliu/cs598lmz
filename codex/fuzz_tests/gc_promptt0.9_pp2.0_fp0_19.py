import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in a multi-threaded setting, with weakrefs
# in a module namespace.

import _weakref

class Foo:
    def __init__(self):
        self.baz = weakref.ref(self)
        
    def boom(self):
        print self
        print self.baz()
        
def worker():
    for i in range(1,100):
        f = Foo()
        f.boom()

t = threading.Thread(target=worker)
t.start()

# Give worker thread time to create weakrefs galore.
import time
time.sleep(0)

# This should collect all f objects created by worker thread
gc.collect()

# The worker thread may still be running, so explicitly wait for a while
# more.
for i in range(1,500):
    print i
    # this loop should search through a lot of free lists,
    # and process a lot of weakrefs.
    # Here we hope that the worker thread is trying to collect
    # gc objects.
    gc.collect()
