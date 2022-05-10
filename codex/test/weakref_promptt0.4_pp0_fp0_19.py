import weakref
# Test weakref.ref() on a class instance.
import gc

class C(object):
    pass

c = C()
r = weakref.ref(c)
