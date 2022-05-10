import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects
# that have a __del__.

# We create a bunch of uncollectable objects with __del__
# methods.  We then collect, and make sure __del__ is called.

# This test has two parts.  The first part creates objects
# with a __del__ methods that raise an exception.  The second
# part creates objects with a __del__ method that sets a flag.

# When run normally, this test should print "no errors".
# It should not cause any core dumps or assert failures.

import sys
import gc

# if 1:
#     class A:
#         def __del__(self):
#             raise SystemError

#     for i in range(1000):
#         x = A()

#     gc.collect()

#     for i in range(1000):
#         if not gc.garbage:
#             break
#         print(gc.garbage.pop())

#     print("no errors")

# if 1:
#     class A:
#         def __del__(self
