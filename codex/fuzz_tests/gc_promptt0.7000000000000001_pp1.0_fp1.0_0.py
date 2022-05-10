import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
n = 50000
#
# Test that instances can be collected
#
print 'Testing instances'
for i in range(n):
    x = C()
    x = None  # Create a lot of instances, then let them go out of scope
print "Collected", gc.collect()

#
# Test cyclic gc
#
print 'Testing cycles'
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

o = D()
o.a = A()
o.b = B()
o.c = C()
o.d = D()
for o in (o, o.a, o.b, o.c, o.d):
    o.o = o
del o
print "Collected", gc.collect()

#
# Test gc of module globals
#
print 'Testing module globals'
for i in range(n):
    mod = __import__(__name__)
    mod = None
print "Collected", g
