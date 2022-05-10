import weakref
# Test weakref.ref:

# Create a simple object:

class C(object):
    pass

obj = C()
obj.x = 10

# Create a weakref with a callable:

r1 = weakref.ref(obj, lambda x: obj == None)
print obj.x, r1()

# Create a weakref without a callable:

r2 = weakref.ref(obj)
print obj.x, r2()

# Create a cyclic reference object:

obj.next = obj
r3 = weakref.ref(obj)

# This will fail with a reference count error if the
# circular reference is not treated correctly by
# the weakref:

obj.x = 20
print obj.x, r3()

# Create an explicit reference cycle (same as for
# obj.next above):

del obj.next
obj.next = obj

# Create a weakref with a callable:

r4 = weakref.ref(obj, lambda x: obj == None)
print obj.x, r4()

# Create a weakref without
