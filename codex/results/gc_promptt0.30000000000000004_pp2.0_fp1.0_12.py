import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky.  We want to make sure that gc.collect()
# collects everything it should collect, and that it doesn't collect
# anything it shouldn't collect.  We also want to make sure that
# gc.collect() doesn't collect anything if there's nothing to collect.
#
# To do this, we create a bunch of objects, and then we create a bunch
# of cycles.  We then collect, and make sure that the objects in the
# cycles are not collected.  We then break the cycles, and collect
# again, and make sure that the objects in the cycles *are* collected.
#
# In addition, we make sure that gc.collect() doesn't collect anything
# if there's nothing to collect.

# Create a bunch of objects
objects = [C(), C(), C(), C(), C(), C(), C(), C(), C(), C()]

# Create a bunch of cycles
objects.append(objects)
objects.append([objects, objects])
objects.append([objects[:], objects[:]])
objects.append([objects[:], objects
