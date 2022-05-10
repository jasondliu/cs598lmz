import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

class A:
    def m(self):
        pass

class B:
    def m(self):
        pass

class C:
    def m(self):
        pass

class D:
    def m(self):
        pass

a = A()
b = B()
c = C()
d = D()

assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert type(A.m) == types.FunctionType
assert type(B.m) == types.FunctionType
assert type(a.m) == types.FunctionType
assert type(b.m) == types.FunctionType
assert type(c.m) == types.FunctionType
assert type(d.m) == types.FunctionType

# Test types.MethodType
class E:
    def m(self):
        pass

class F:
    def m(self):
        pass

e = E()
f = F()

assert type(e.m) ==
