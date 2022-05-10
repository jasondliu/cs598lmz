import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs to old-style classes.
class A(object):
    pass

class B:
    pass
a = A()
b = B()
ra = weakref.ref(a)
rb = weakref.ref(b)

import gc
gc.collect()
gc.collect()
print(gc.garbage)
