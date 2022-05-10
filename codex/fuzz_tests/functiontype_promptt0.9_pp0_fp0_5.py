import types
# Test types.FunctionType

def foo():
    """docstring"""
    return 'foo'

class A:
    """docstring for A"""
    pass

class B(A):
    """docstring for B"""
    def f():
        """docstring for f"""
        return 'B.f()'

    def f(*args, **kw):
        return 'B.f() *args **kw'

def f(*args):
    """docstring for f"""
    return 'f() *args'

assert isinstance(foo, types.FunctionType)
assert issubclass(type(foo), types.FunctionType)

assert not isinstance(A, type)

assert isinstance(A, types.ClassType)
assert isinstance(B, types.ClassType)
assert issubclass(type(A), types.ClassType)
assert issubclass(type(B), types.ClassType)

assert isinstance(B.f, types.MethodType)
assert isinstance(B().f, types.MethodType)
assert issubclass(type(B.f), types.Method
