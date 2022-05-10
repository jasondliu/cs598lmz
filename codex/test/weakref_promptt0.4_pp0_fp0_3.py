import weakref
# Test weakref.ref() with a class instance.
import weakref
import gc

class C:
    pass

c = C()
r = weakref.ref(c)
