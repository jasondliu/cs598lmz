import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a class that has a __del__ method that
# calls gc.collect()

class A:
    def __del__(self):
        gc.collect()

a = A()
a = 1
gc.collect()

# Test gc.collect() with a class that has a __del__ method that
# calls gc.collect() and a __repr__ method that calls gc.collect()

class B:
    def __del__(self):
        gc.collect()
    def __repr__(self):
        gc.collect()
        return "<B instance>"

b = B()
b
gc.collect()

# Test gc.collect() with a class that has a __del__ method that
# calls gc.collect() and a __str__ method that calls gc.collect()

class C:
    def __del__(self):
        gc.collect()
    def __str__(self):
        gc.collect()
        return "C instance"

c = C()
str(c)
gc.
