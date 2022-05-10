import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a cycle
class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
a.b = None
b.a = None
a = b = None
class A:
    def __del__(self):
        print "A.__del__"

a = A()
b = A()
a.b = b
b.a = a
a.b = None
b.a = None
a = b = None
gc.collect()
print "Expect A.__del__ twice"
class A:
    def __del__(self):
        print "A.__del__"

a = A()
b = A()
a.b = b
b.a = a
a.b = None
b.a = None
a = b = None
gc.collect()
print "Expect A.__del__ twice"
class A:
    pass

weakref.ref(A)
gc.collect()
print "Expect nothing"
class A:
    def __del__(self):
