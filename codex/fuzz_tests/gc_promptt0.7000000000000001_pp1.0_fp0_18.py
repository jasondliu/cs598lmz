import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at every call
gc.set_threshold(0, 0, 0)

# Create a class with a __del__ method to verify that it is called.
# The object of this class should never be collectable.
class C:
    def __del__(self):
        print("__del__ called")

# Create a class with a __del__ method to verify that it is called.
# The object of this class should never be collectable.
class D:
    def __del__(self):
        print("__del__ called")

# Create a class with a __del__ method to verify that it is called.
# The object of this class should never be collectable.
class E:
    def __del__(self):
        print("__del__ called")

# The object should be collectable.
class F:
    def __del__(self):
        print("__del__ called")

# A class with a weakref-able slot
class G:
    pass

# A class with a weakref-able slot
class H:
    pass

# A class
