import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class B(object):
    pass

def f(self):
    return self.x

B.m = types.MethodType(f, None, B)

# Test that we can create a method with a non-string name
class C(object):
    pass

def g(self):
    return self.x

C.m = types.MethodType(g, None, C)

# Test that we can create a method with a non-string name
class D(object):
    pass

def h(self):
    return self.x

D.m = types.MethodType(h, None, D)

