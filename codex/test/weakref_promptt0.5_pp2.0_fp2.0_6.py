import weakref
# Test weakref.ref()
import gc
import pickle

class C(object):
    pass

o = C()
r = weakref.ref(o)

