import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This is a test to make sure that gc.collect() does not collect
# objects that are still reachable.
#
# It does this by creating an object that has a __del__ method that
# records the object's id in a list.  The object is created with two
# references: one to the object and one to the __del__ method.  If
# the object is collected, then the __del__ method will be called,
# and the object's id will be appended to the list.  If the object is
# not collected, then the __del__ method will not be called, and the
# object's id will not be appended to the list.
#
# The object is created in a function so that the reference to the
# object is local to the function.  This means that when the function
# returns, the only reference to the object will be the reference
# from the object to its __del__ method.  This is enough to keep the
# object from being collected.
#
# The function is called a few times, and then gc.collect() is
# called.  If the
