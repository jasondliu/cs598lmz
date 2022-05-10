import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.DEBUG_COLLECTABLE

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

o = D()

# Build a reference cycle
o.x = o

# Test gc.collect()
gc.collect()

# Test gc.DEBUG_COLLECTABLE
del o
gc.collect()

# Check that gc works with a class defining a custom __del__ method.
class E:
    def __del__(self):
        pass

gc.collect()
e = E()
gc.collect()
del e
gc.collect()

# Check that gc works with a class defining a custom __del__ method
# that raises an exception.
class F:
    def __del__(self):
        raise Exception

gc.collect()
f = F()
gc.collect()
del f
gc.collect()

# Check that gc works with a class defining a custom __del__ method
# that raises an exception and with a
