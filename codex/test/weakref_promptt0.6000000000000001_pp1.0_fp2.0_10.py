import weakref
# Test weakref.ref class.
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

