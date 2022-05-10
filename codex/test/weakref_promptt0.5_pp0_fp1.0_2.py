import weakref
# Test weakref.ref.__call__

import weakref
import gc

class A(object):
    pass

a = A()
ref = weakref.ref(a)

del a
gc.collect()

try:
    ref()
except ReferenceError:
    pass
else:
    raise RuntimeError("ref() should raise ReferenceError")

try:
    ref()
except ReferenceError:
    pass
else:
    raise RuntimeError("ref() should raise ReferenceError")
