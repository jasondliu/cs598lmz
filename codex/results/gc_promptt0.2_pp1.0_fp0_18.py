import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# A class with a __del__ method
class A:
    def __del__(self):
        print "A.__del__"

# A class with a weakref-able method
class B:
    def __init__(self):
        self.a = A()
    def __del__(self):
        print "B.__del__"

# A class with a weakref-able method
class C:
    def __init__(self):
        self.a = A()
    def __del__(self):
        print "C.__del__"

# A class with a weakref-able method
class D:
    def __init__(self):
        self.a = A()
    def __del__(self):
        print "D.__del__"

# A class with a weakref-able method
class E:
    def __init__(self):
        self.a = A()
    def __del__(self):
        print "E.__del__"

# A class with a weakref-able method
