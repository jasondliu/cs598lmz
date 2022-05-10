import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a class and an instance of a class.
# Collecting the instance should not collect the class.
# (This is a repeat of a test in gc_list_tests.py)

class C:
    def __init__(self):
        self.x = 1

c = C()
wc = weakref.ref(c)
wc() is c

# This should not collect the class.
gc.collect()
wc() is c

# This should collect the instance.
del c
gc.collect()
wc() is None

# This should not collect the class.
gc.collect()

# This should collect the class.
del C
gc.collect()

# The following tests check whether __del__ methods are executed when
# a class or a type is collected.

class C:
    def __del__(self):
        print("__del__ called")

c = C()
wc = weakref.ref(c)
wc() is c

# This should not collect the class.
gc.collect()
wc() is c
