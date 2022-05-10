import types
types.MethodType(foo, [], foo.__class__)()

class A(object):
    @staticmethod
    def foo():
        print "A"

A.foo()
objA = A()
objA.foo()
t = type(A)
objt = t()
objt.foo()

class B(object):
    @classmethod
    def bar(cls):
        print "B"

B.bar()
objB = B()
objB.bar()
