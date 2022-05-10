import weakref
# Test weakref.ref on list objects.
# This test should succeed by not crashing.
class A(object):
    pass

x = A()
l = [x, x]
wr = weakref.ref(l)
del l
del x
collect()
print wr()
