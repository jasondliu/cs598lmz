import types
types.MethodType(__new__,None, type)

# tests for __class__


class A(object):
    def foo(self):
        return "A"

class B(A):
    def foo(self):
        return "B"

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

i1 = A()
i2 = B()
i3 = C()
i4 = D()
i5 = E()

i1.__class__
i1.__class__ = D
i1.__class__
i1.foo()

i1.__class__ = C
i1.__class__
i1.foo()

i2.__class__ = A
i2.__class__
i2.foo()

i2.__class__ = D
i2.__class__
i2.foo()

i3.__class__ = A
i3.__class__
i3.foo()

i3.__class__ = B
i3
