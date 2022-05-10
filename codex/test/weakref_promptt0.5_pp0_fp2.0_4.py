import weakref
# Test weakref.ref()
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)
o2 = r()
