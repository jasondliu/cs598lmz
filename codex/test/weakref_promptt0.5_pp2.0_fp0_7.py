import weakref
# Test weakref.ref() by making sure that the referent is not kept alive by the
# reference.

import gc

class C:
    pass

o = C()
r = weakref.ref(o)

del o
gc.collect()

print(r())
