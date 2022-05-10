import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A:
    pass
x = A()
w = weakref.ref(x)
print w() is None
print w
print x
x = A()
print w() is None
print w
print x

# Test gc.collect
class A:
    pass
x = A()
x.x = x
w = weakref.ref(x)
print w() is None
print w
print x
x = A()
x.x = x
print w() is None
print w
print x

# Test gc.collect
class A:
    def __del__(self):
        print "A.__del__"
x = A()
w = weakref.ref(x)
print w() is None
print w
print x
x = A()
print w() is None
print w
print x

# Test gc.collect
class A:
    def __del__(self):
        print "A.__del__"
x = A()
x.x = x
w = weakref.ref(x)
print w() is None
