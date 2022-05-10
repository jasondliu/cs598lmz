import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.

class A:
    pass

class B(A):
    pass

class Collectable:
    def __init__(self):
        self.a = A()
        self.b = B()

# Create a reference cycle.
ob1 = Collectable()
ob2 = Collectable()
ob1.next = ob2
ob2.next = ob1
del ob1, ob2
gc.collect()
# Create an uncollectable cycle.
ob1 = A()
ob2 = B()
ob1.next = ob2
ob2.next = ob1
del ob1, ob2
gc.collect()
# Create an uncollectable cycle with a __del__ method.
class C:
    def __del__(self):
        pass

ob1 = C()
ob2 = C()
ob1.next = ob2
ob2.next = ob1
del ob1, ob2
gc.collect()
# Create an uncollectable cycle with a __del__ method that triggers a
# collection.
class D:
    def
