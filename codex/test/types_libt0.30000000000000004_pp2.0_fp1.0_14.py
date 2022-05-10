import types
types.MethodType(lambda self: None, None, None)

# Test that the __init__ method is not inherited
class A(object):
    def __init__(self):
        pass

class B(A):
    pass

B()

# Test that the __new__ method is not inherited
class A(object):
    def __new__(cls):
        return object.__new__(cls)

class B(A):
    pass

B()

# Test that the __del__ method is not inherited
class A(object):
    def __del__(self):
        pass

class B(A):
    pass

B()

# Test that the __getattr__ method is not inherited
class A(object):
    def __getattr__(self, name):
        pass

class B(A):
    pass

B()

# Test that the __setattr__ method is not inherited
class A(object):
    def __setattr__(self, name, value):
        pass

class B(A):
    pass


