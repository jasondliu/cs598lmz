import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __del__(self):
        print "A.__del__"

a = A()
a = None
gc.collect()
print

# Test gc.garbage

class B:
    def __del__(self):
        print "B.__del__"

b = B()
b = None
gc.garbage.append(b)
del b
gc.collect()
print

# Test weakrefs

class C:
    def __del__(self):
        print "C.__del__"

c = C()
c = None
w = weakref.ref(c)
gc.collect()
print

# Test __del__ methods that raise exceptions

class D:
    def __del__(self):
        print "D.__del__"
        raise Exception

d = D()
d = None
gc.collect()
print

# Test __del__ methods that raise exceptions

class E:
    def __del__(self):
        print "E.__del__"

