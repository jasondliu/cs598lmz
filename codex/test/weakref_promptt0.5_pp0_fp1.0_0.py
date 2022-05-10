import weakref
# Test weakref.ref
import gc
import sys

class C:
    pass

o = C()
r = weakref.ref(o)

