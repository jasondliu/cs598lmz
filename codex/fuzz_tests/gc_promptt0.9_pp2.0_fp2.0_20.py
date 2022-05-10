import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on old-style instances with finalizers and weakrefs

import weakref

class Spam:
    def __del__(self):
        global sideeffect3
        sideeffect3 = self

def somefunc():
    s = Spam()
    r = weakref.ref(s)
    del s
    gc.collect()

somefunc() # the collect() should
