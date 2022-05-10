import weakref
# Test weakref.ref() explicitly.

class A(object):
    pass

a = A()
class B(object):
    def __init__(self, a):
        self.a = a

b = B(a)
b.a

c = weakref.ref(a)

# test call
va = weakref.ref(a)
va() is a

# define a function that calls weakref.ref
def f(a):
    return weakref.ref(a)

# test that weakref.ref() is called implicitly
va = f(a)
va() is a

# define a function that takes a weakref.ref as an argument
def g(w):
    return w()

va = f(a)
va() is g(va)
va() is g(va)
g(c) is a
vr = weakref.ref(a)
vr
vr() is a
vr
vr() is a
vr
vr1 = weakre
