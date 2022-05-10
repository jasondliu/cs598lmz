import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc._collect()
gc._collect()
print_counts()

import sys
print_counts()

print 'garbage:', gc.garbage
del gc.garbage[:]

print_counts()

class C:
    pass

c = C()
c.foo = C()
print_counts()

#c = None
#print_counts()
#del c
