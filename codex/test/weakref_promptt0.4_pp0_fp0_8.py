import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
a.x = A()
a.x.y = A()
a.x.y.z = a

x = weakref.ref(a)
