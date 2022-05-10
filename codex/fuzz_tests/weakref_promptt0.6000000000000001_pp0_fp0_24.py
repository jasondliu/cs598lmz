import weakref
# Test weakref.ref() in a function.
def f():
    l = [1, 2, 3]
    r = weakref.ref(l)
    return r

x = f()
print x()
del l
print x()

class A(object):
    def __init__(self):
        self.x = 42

# Test weakref.ref() in a method.
def g(self):
    r = weakref.ref(self)
    return r

a = A()
a.f = g
x = a.f()
print x().x
del a
print x()

# Test weakref.ref() on a class.
C = weakref.ref(A)
print C() is A
del A
print C()

# Test weakref.proxy() in a function.
def f():
    l = [1, 2, 3]
    p = weakref.proxy(l)
    return p

x = f()
print len(x)
del l
try:
    len(x)
except ReferenceError:
    pass
else:

