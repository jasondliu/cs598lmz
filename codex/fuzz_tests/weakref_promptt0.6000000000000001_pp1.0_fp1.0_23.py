import weakref
# Test weakref.ref(self) within a class.

class A:
    def __init__(self):
        self.b = weakref.ref(self)

    def test(self):
        if self.b() is not self:
            raise RuntimeError, "wrong self"

a = A()
a.test()

class B(A):
    def test(self):
        if self.b() is not self:
            raise RuntimeError, "wrong self"

b = B()
b.test()

class C(A):
    def __init__(self):
        A.__init__(self)
    def test(self):
        if self.b() is not self:
            raise RuntimeError, "wrong self"

c = C()
c.test()

class D(A):
    def __init__(self):
        A.__init__(self)
    def test(self):
        if self.b() is not self:
            raise RuntimeError, "wrong self"

d = D()
d.test()

class E(A
