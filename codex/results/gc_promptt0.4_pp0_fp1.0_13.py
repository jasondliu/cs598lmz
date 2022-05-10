import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
    def __del__(self):
        print "A.__del__"

class B:
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "B.__del__"

a = A()
a.b
print "Collecting..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()
print n, "unreachable"
print "Collecting again..."
n = gc.collect()

