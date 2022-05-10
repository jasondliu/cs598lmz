import weakref
# Test weakref.ref()
class A:
    pass
a = A()
wr = weakref.ref(a)
