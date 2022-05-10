import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakrefable object that has a finalizer.
class A(object):
    def __del__(self):
        pass

a = A()
a_wr = weakref.ref(a)
a_wr
a = None
gc.collect()
a_wr() is None
del a_wr
gc.collect()
# Create objects with a refcount of 1 (i.e. the original reference,
# not counting the reference from gc.garbage).

# Case 1: the object has a finalizer, but it's not weakrefable
class A(object):
    def __del__(self):
        print "A.__del__"

class B(object):
    def __del__(self):
        print "B.__del__"
        a1.b = a2

a1=A()
a2=A()

a1.b = a2
b = B()
a2.b = b
del a1
del a2
del b
gc.collect()
gc.garbage
# Case 2: the object is weak
