import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class B(object):
    pass

b = B()
b.f = types.MethodType(lambda self: self.x, None, B)

# Test that we can create a method with a non-string name
class C(object):
    pass

c = C()
c.f = types.MethodType(lambda self: self.x, None, C)

# Test that we can create a method with a non-string name
class D(object):
    pass

d = D()
d.f = types.MethodType(lambda self: self.x, None, D)

# Test that we can create a method with a non-string name
class E(object):
    pass

e = E()
e.f = types.MethodType(lambda self: self.x, None, E)

# Test that we can create a method with a non-string name
class F(object):
    pass

f = F()
f
