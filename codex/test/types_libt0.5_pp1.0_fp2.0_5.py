import types
types.MethodType(lambda self: None, None)

# classes
class C(object):
    pass

# static methods
class D(object):
    @staticmethod
    def foo():
        pass

# class methods
class E(object):
    @classmethod
    def foo(cls):
        pass

