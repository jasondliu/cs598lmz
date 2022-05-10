import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test should be run with the -M option to test the
# automatic collection of cyclic garbage.
#
# The test creates a cyclic garbage object and then
# checks that it is collected.  The test then creates
# a cyclic garbage object with a finalizer and checks
# that the finalizer is called.
#
# The test should be run with the -v option to see
# the finalizers being called.

import gc

class A:
    def __del__(self):
        print "deleting A"

def callback(ignored):
    print "calling back"

# Create a cyclic garbage object
a = A()
b = A()
a.x = b
b.x = a

# Check that it is collected
del a, b
gc.collect()

# Create a cyclic garbage object with a finalizer
a = A()
b = A()
a.x = b
b.x = a
wr = weakref.ref(a, callback)

# Check that the finalizer is called
del a, b

