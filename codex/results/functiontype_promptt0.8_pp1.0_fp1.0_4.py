import types
# Test types.FunctionType


def foo():
    pass


class A:
    pass


class B(A):
    pass


class D:

    def __init__(self):
        pass

    def _test(self):
        pass

    def __test(self):
        pass

    def __test2__(self):
        pass

    def __call__(self):
        pass

a = A()
b = B()
inst = D()


def test_function_type():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(A, types.FunctionType)
    assert not isinstance(a, types.FunctionType)
    assert not isinstance(b, types.FunctionType)
    assert not isinstance(D.__init__, types.FunctionType)
    assert not isinstance(D.__test, types.FunctionType)
    assert not isinstance(D._test, types.FunctionType)
    assert not isinstance(D.__test2__, types.FunctionType)
    assert not isinstance(D.__call__, types.Function
