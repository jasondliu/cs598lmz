import types
types.MethodType(lambda self: None, None, cls)

# Test that we can create a bound method from a class method
class cls:
    @classmethod
    def f(cls):
        pass

types.MethodType(cls.f, None, cls)

# Test that we can create a bound method from a static method
class cls:
    @staticmethod
    def f():
        pass

types.MethodType(cls.f, None, cls)

# Test that we can create a bound method from a function
def f():
    pass

types.MethodType(f, None, cls)

# Test that we can create a bound method from a lambda
types.MethodType(lambda self: None, None, cls)
