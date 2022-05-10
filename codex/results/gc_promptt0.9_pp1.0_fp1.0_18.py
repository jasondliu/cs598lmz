import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
# Test that cyclic gc works.
# Test the weak reference support.
import types
class A:
    pass

class B(A):
    pass

class C(A):
    pass

gc.collect()
a = A()
b = B()
c = C()

#print gc.collect()
#print len(gc.garbage)
#del a
#print gc.collect()
#print len(gc.garbage)
#del b
#print gc.collect()
#print len(gc.garbage)
#del c
#print gc.collect()
#print len(gc.garbage)

a.b = b
b.a = a
a.c = c
c.a = a

#print gc.collect()
#print len(gc.garbage)
del a
del b
del c
#print gc.collect()
#print len(gc.garbage)
#print gc.garbage[0].__dict__.keys()
#print gc.garbage[1].__
