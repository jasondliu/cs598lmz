import weakref
# Test weakref.ref(...)
class A(object):
    pass

a = A()

class B(object):
    pass

b = B()
b.a = a

# ref(a) returns a weakref to a
ra = weakref.ref(a)

# ref(b) returns a weakref to b
rb = weakref.ref(b)

# ref(b.a) returns a weakref to what b.a referred to: a
# (note that ref(b.a) is equivalent to ref(getattr(b, 'a')) )
rab = weakref.ref(b.a)

# a and b are still in scope and their refcount is 2

# ref(a) and ref(b) are still alive, but their refcount is 1

# ref(b.a) is still alive and its refcount is 1

# delete a, and its refcount becomes 0
del a

# a is now gone, but b is still in scope

# ref(a) is now dead and its refcount is 0

# ref(b) is still
