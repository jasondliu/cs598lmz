import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can create a method from a lambda in a class
class B(object):
    def __init__(self):
        self.x = 42
        self.m = types.MethodType(lambda self: self.x, self, B)

# Test that we can create a method from a lambda in a class
class C(object):
    def __init__(self):
        self.x = 42
        self.m = types.MethodType(lambda self: self.x, self, C)

# Test that we can create a method from a lambda in a class
class D(object):
    def __init__(self):
        self.x = 42
        self.m = types.MethodType(lambda self: self.x, self, D)

# Test that we can create a method from a lambda in a class
class E(object):
    def __init__(self):
        self.x = 42
        self.m = types.MethodType(lambda self: self.x, self, E)

