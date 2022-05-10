import weakref
# Test weakref.ref
import gc

class A:
    pass

class B:
    pass

a = A()
b = B()
a.attr = b
b.attr = a

r = weakref.ref(a)
