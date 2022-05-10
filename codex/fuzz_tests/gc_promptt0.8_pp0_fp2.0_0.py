import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# test that gc.collect() calls tp_clear on all collectable objects

class Leak:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "   Deleting", self.name

def f():
    print "Creating",
    a = Leak("a")
    print "Creating",
    b = Leak("b")
    print "   f() returns"
    return a

def g(a):
    print "Creating",
    c = Leak("c")
    print "Creating",
    d = Leak("d")
    print "   a.name is", a.name
    print "   g() returns"

print "Testing gc.collect()"
a = f()
g(a)
a = None
gc.collect()

print
print "Testing gc.disable()"
a = Leak("a")
gc.disable()
print "Creating",
b = Leak("b")
gc.enable()
print "   gc.enable()
