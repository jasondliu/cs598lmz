import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() for objects with a __del__ method

class A:
    def __init__(self):
        self.n = 1
    def __del__(self):
        print ("del", self.n)

a = A()
del a
gc.collect()
# Test gc.collect() for objects with a __del__ method and a cycle

class A:
    def __init__(self):
        self.b = B(self)
    def __del__(self):
        print ("del A")

class B:
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print ("del B")

a = A()
del a
gc.collect()
# Test gc.collect() for objects with a __del__ method and a cycle

class A:
    def __init__(self):
        self.b = B(self)
    def __del__(self):
        print ("del A")

class B:
    def __init__(self, a):
        self.a
