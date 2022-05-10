import weakref
# Test weakref.ref()

import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print 'o:', o
print 'ref:', r
print 'r():', r()

del o
print 'gc.collect():'
gc.collect()
print 'r():', r()

print 'o:', o
print 'ref:', r
print 'r():', r()

del o
print 'gc.collect():'
gc.collect()
print 'r():', r()
