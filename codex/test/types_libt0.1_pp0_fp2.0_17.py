import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class B(object):
    pass

B.__dict__['foo'] = types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class C(object):
    pass

C.__dict__['foo'] = types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class D(object):
    pass

D.__dict__['foo'] = types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method with a non-string name
class E(object):
    pass

E.__dict__['foo'] = types.MethodType(lambda self: self.x, None, A)

