import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

