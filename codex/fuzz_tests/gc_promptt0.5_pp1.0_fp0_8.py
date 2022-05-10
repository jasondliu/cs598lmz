import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in various situations

# Test 1: collect a trivial chain
a = []
b = [a, a]
del a
gc.collect()

# Test 2: collect a cycle
a = []
b = [a]
a.append(b)
del a, b
gc.collect()

# Test 3: collect a cycle with a finalizer
class A:
    def __del__(self):
        pass
a = A()
b = [a]
a.x = b
del a, b
gc.collect()

# Test 4: collect a cycle with a finalizer that resurrects an object
class A:
    def __del__(self):
        self.b = 1
a = A()
b = [a]
a.x = b
del a, b
gc.collect()

# Test 5: collect a cycle with a finalizer that resurrects an object
#         with a finalizer
class A:
    def __del__(self):
        self.b = B()
class B:
    def __del__(self):
        pass
a
