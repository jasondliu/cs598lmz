import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by counting all instances of a class,
# and making sure that the collector removes all dead references.
number_of_instances = 0
class InstanceCounter:
    def __init__(self):
        global number_of_instances
        number_of_instances = number_of_instances + 1
    def __del__(self):
        global number_of_instances
        number_of_instances = number_of_instances - 1

# We start with a clean slate
gc.collect()

# Create an instance of InstanceCounter, and keep a reference
# to it.
i = InstanceCounter()

# Create a second reference to it.
j = i

# Create a weak reference to it.
w = weakref.ref(i)

# Create a cycle, so that the instance will be uncollectable.
i.other = i

# Force a collection, and make sure that the instance is still
# alive.
gc.collect()
if number_of_instances != 1:
    raise TestFailed("%d instances alive after collection" %
