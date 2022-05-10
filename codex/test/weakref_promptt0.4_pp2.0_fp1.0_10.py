import weakref
# Test weakref.ref

import weakref
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)

