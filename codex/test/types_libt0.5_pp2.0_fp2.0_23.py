import types
types.MethodType(m, None, A)

# Test that we can create a method with a classmethod as the function
class A(object):
    pass
class B(object):
    @classmethod
    def m(cls):
        return cls

A.m = types.MethodType(B.m, None, A)

# Test that we can create a method with a staticmethod as the function
class A(object):
    pass
class B(object):
    @staticmethod
    def m():
        return None

A.m = types.MethodType(B.m, None, A)

# Test that we can create a method with a classmethod as the function
class A(object):
    pass
class B(object):
    def m(self):
        return self

A.m = types.MethodType(B.m, None, A)

# Test that we can create a method with a classmethod as the function
class A(object):
    pass
class B(object):
    def m(self):
        return self

A.m = types
