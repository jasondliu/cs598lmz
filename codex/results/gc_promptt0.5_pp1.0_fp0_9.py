import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Test case 1:
# Check that collect() returns the number of unreachable objects with
# DELAYED (cyclic) deallocation

class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

del a, b
gc.collect()

# Test case 2:
# Check that collect() returns the number of unreachable objects with
# FINALIZERS deallocation

class C:
    def __del__(self):
        pass

c = C()

del c
gc.collect()

# Test case 3:
# Check that collect() returns the number of unreachable objects with
# WEAKREF deallocation

class D:
    pass

d = D()

def callback(obj):
    pass

w = weakref.ref(d, callback)

del d
gc.collect()

# Test case 4:
# Check that collect() returns the number of unreachable objects with
# GENERATIONS deallocation

class E:

