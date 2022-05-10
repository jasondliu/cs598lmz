import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakref and callback

# This test is currently disabled because it is too slow.

# import sys
# import gc
# import weakref

# class A:
#     pass

# class B:
#     pass

# callback_called = 0
# def callback(x):
#     global callback_called
#     print "callback called with", x
#     callback_called += 1

# a = A()
# a.b = B()
# a.b.a = a

# gc.collect()
# r = weakref.ref(a.b, callback)
# gc.collect()
# del a
# gc.collect()
# if callback_called:
#     raise "callback called too soon"
# del r
# gc.collect()
# if callback_called:
#     raise "callback called too soon"
# #
# # Now try again, but with a strong reference to the callback function
# #
# callback_called = 0
# a = A()
# a.b = B()
# a.b.a =
