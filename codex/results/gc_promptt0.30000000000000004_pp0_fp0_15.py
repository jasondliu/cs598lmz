import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is not exhaustive.  It only checks that collect() does
# not crash, and that it collects objects that are collectable.
#
# Objects are collectable if they are not part of a reference cycle
# involving objects that have an __del__() method.  (Objects with an
# __del__() method are not collectable.)  The test does not check
# whether collect() collects objects that are part of reference cycles
# that include objects with an __del__() method.

# This test is not exhaustive.  It only checks that collect() does
# not crash, and that it collects objects that are collectable.
#
# Objects are collectable if they are not part of a reference cycle
# involving objects that have an __del__() method.  (Objects with an
# __del__() method are not collectable.)  The test does not check
# whether collect() collects objects that are part of reference cycles
# that include objects with an __del__() method.

import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)

class C:

