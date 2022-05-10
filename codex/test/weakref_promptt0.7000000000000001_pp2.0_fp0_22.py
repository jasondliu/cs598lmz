import weakref
# Test weakref.ref() for objects that don't support weak references.
# This should be a no-op.

class C:
    pass

c = C()
wr = weakref.ref(c)
c is wr()
del c
wr() is None
# Test the basic functionality of weak references.

# Create a cyclic reference between a list and a nested list.

a = []
b = [a]
a.append(b)

# Create a weak reference to the nested list.

wref = weakref.ref(a)

# Remove the cyclic reference.

del a

# Make sure the weak reference can still be used even after the cyclic
# reference is destroyed.

wref()[0][0]
# Make sure we can create weak references to objects that have
# __del__ methods (which are not called as a result).

class D:
    def __del__(self):
        pass

d = D()
wref = weakref.ref(d)
wref()
# Make sure we can create weak references to instances and class objects.

