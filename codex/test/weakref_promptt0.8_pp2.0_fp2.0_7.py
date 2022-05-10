import weakref
# Test weakref.ref of a singleton
class A(object):
    def __init__(self,x):
        self.x = x
        self.wr = weakref.ref(self)

# a = A(2)
a = A(2)
b = a
wr = weakref.ref(a)

print (a is wr())
print (a is b)

A.__init__ = lambda self, x: None
a = A(2)
b = a
wr = weakref.ref(a)

print (a is wr())
print (a is b)


# Test weakref.ref of a class
class B(object):
    def __init__(self,x):
        self.x = x
        self.wr = weakref.ref(self.__class__)

b = B(3)
B.__init__ = lambda self, x: None
b = B(3)

# Test weakref.ref of a constant
class C(object):
    def __init__(self,x):
        self.x = x
