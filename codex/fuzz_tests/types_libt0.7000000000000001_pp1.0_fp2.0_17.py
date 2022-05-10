import types
types.MethodType(test, None, None)

class A(object):
    def __init__(self):
        self.x = 'A'

a = A()

class B(object):
    def __init__(self):
        self.x = 'B'

b = B()

b.__class__ = A
print b.x

a = A()
a.__class__ = B
print a.x

class Foo(object):
    def __init__(self):
        print 'foo'

print type(Foo.__new__)
print type(A.__init__)

class C(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
    def __init__(self):
        print 'C init'

c = C()

class D(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(Foo, *args, **kwargs
