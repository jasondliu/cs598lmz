import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "Foo(%r)" % self.x

class Bar(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "Bar(%r)" % self.x

print "Testing gc.collect()..."

# Create a bunch of objects, and make sure they are all collected.
# This tests the gc list stuff, the generation 0 and 1 code, and
# the non-generational code.

print "   - test1"

# This tests a particularly tricky case for the Python GC:  when
# the last reference to an object is in a container that is being
# tracked by the GC, but the object is not itself being tracked
# by the GC.  This used to crash Python.

# XXX This test is currently disabled, because the test case no
# longer crashes Python.  It does still cause the GC to do a lot
#
