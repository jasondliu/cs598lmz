import weakref
# Test weakref.ref() in a class

class A:
    pass

class B(A):
    pass

a = A()
b = B()

wr1 = weakref.ref(a)
wr2 = weakref.ref(b)

