import types
# Test types.FunctionType

def test_functiontype():
    def foo(x, y):
        return x + y

    assert isinstance(foo, types.FunctionType)
    assert not isinstance(foo, types.LambdaType)
    assert foo(1, 2) == 3

# Test types.LambdaType

def test_lambdatype():
    foo = lambda x, y: x + y

    assert isinstance(foo, types.LambdaType)
    assert not isinstance(foo, types.FunctionType)
    assert foo(1, 2) == 3

# Test types.BuiltinFunctionType

def test_builtinfunctiontype():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert len([1, 2, 3]) == 3

# Test types.BuiltinMethodType

def test_builtinmethodtype():
    class Foo(object):
        def __len__(self):
            return 3

    assert isinstance(Foo.__len__, types.BuiltinMethod
