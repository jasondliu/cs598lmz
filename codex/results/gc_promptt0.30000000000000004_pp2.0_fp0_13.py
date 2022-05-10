import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __del__(self):
        print "A.__del__"

a = A()
a = None
gc.collect()

# Test gc.garbage

class B:
    def __del__(self):
        print "B.__del__"

b = B()
gc.garbage.append(b)
b = None
gc.collect()

# Test gc.get_objects()

class C:
    def __del__(self):
        print "C.__del__"

c = C()
gc.get_objects()
c = None
gc.collect()

# Test gc.get_referrers()

class D:
    def __del__(self):
        print "D.__del__"

d = D()
gc.get_referrers(d)
d = None
gc.collect()

# Test gc.get_referents()

class E:
    def __del__(self):
        print "E.__del__"
