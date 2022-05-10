import types
types.MethodType(foo, x)

def bar(self, a, b, c):
    return self, a, b, c

x.bar = types.MethodType(bar, x, x.__class__)
x.bar(1, 2, 3)
x.bar(a=1, b=2, c=3)

def bar(self, a, b, c):
    return self, a, b, c

types.MethodType(bar, x, x.__class__)

class A(object):
    def foo(self):
        return self

a = A()
a.foo()

class B(A):
    pass

b = B()
b.foo()

class C(object):
    def foo(self):
        return self

c = C()
c.foo()

class D(C):
    pass

d = D()
d.foo()

