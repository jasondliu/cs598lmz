import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by counting the number of
# unreachable objects collected by it.
# This count may be incremented by other threads
# between calls to gc.collect(), of course.
#
# The test takes some time, so  at the end of it
# the number of objects collected is printed.
# The test can be run with different options for
# the garbage collector.  With the default options,
# this number should be around 3e5 on a linux/i386 box
# with around 1.5GB of memory.  Without the patch
# for issue #5775, the number is around 3e4.

count = [0, 0]
def callback(count=count):
    count[0] = count[0] + 1

# A class with one instance per collectable object
class C(object):
    pass

def f(count=count):
    objects = [C() for i in range(count[1])]
    # Create a cycle with all the objects
    objects.append(objects)
    # Remove the reference to the list
    del objects
    # Force a collect
    gc
