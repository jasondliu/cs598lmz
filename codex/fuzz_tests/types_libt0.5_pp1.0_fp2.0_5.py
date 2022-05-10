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

# old-style classes
class F:
    pass

# old-style static methods
class G:
    def foo():
        pass
    foo = staticmethod(foo)

# old-style class methods
class H:
    def foo(cls):
        pass
    foo = classmethod(foo)
