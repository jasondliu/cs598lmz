import weakref
# Test weakref.ref()
import operator


class C:
    pass

o = C()
r = weakref.ref(o)
