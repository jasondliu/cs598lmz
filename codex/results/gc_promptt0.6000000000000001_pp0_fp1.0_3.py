import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() collects
# cyclic garbage.
#
# The cyclic garbage is created by a function
# that creates a cycle of objects, then returns
# the last object in the cycle.
#
# The test uses a weak reference to the last
# object in the cycle to determine if the cycle
# has been collected.  If the cycle is not
# collected, the weak reference will be valid.
#
# The test also checks that gc.collect() collects
# cyclic garbage that has been created by a
# function that has been called, but is no
# longer referenced.
#
# The cyclic garbage is created by a function
# that creates a cycle of objects, then returns
# the last object in the cycle.
#
# The test uses a weak reference to the last
# object in the cycle to determine if the cycle
# has been collected.  If the cycle is not
# collected, the weak reference will be valid.
#
# The test also checks that gc.collect() collects
# cyclic garbage that has been created by a
# function that has been
