import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print "A.__del__"

class B:
    def __del__(self):
        print "B.__del__"

class C:
    def __del__(self):
        print "C.__del__"

class D:
    def __del__(self):
        print "D.__del__"

a = A()
b = B()
c = C()
d = D()

a.b = b
b.c = c
c.d = d
d.a = a

#a = b = c = d = None
del a, b, c, d
gc.collect()

# Test gc.garbage
class A:
    def __del__(self):
        print "A.__del__"

class B:
    def __del__(self):
        print "B.__del__"

class C:
    def __del__(self):
        print "C.__del__"

class D:
   
