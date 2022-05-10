import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(generation=0)

gc.collect()
gc.collect(0)
# Test gc.collect(generation=1)

gc.collect()
gc.collect(1)
# Test gc.collect(generation=2)

gc.collect()
gc.collect(2)
# Test gc.collect()

l = []

for i in range(10):
    l.append(l)

del l

gc.collect()
gc.collect(999)
gc.collect()
gc.collect(generation=0)
gc.collect(generation=1)
gc.collect(generation=2)
gc.collect(generation=3)

import gc, weakref
class Test:       # Class with cyclic references
    def __init__(self):
        self.ref = self
a = Test()
b = Test()
c = Test()
a.ref = b
b.ref = c
c.ref = a
del c,b,a
# At this point, no reference to these objects exist.
# So, they can't be traced by Python
