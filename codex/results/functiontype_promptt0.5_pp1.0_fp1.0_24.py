import types
# Test types.FunctionType

def foo():
    pass

class A(object):
    def bar(self):
        pass

def test_function():
    assert isinstance(foo, types.FunctionType)
    assert not isinstance(A, types.FunctionType)
    assert not isinstance(A.bar, types.FunctionType)
    assert not isinstance(A().bar, types.FunctionType)

# Test types.LambdaType

def test_lambda():
    assert isinstance((lambda x: x), types.LambdaType)
    assert isinstance((lambda x, y: x), types.LambdaType)
    assert isinstance((lambda x, y, z: x), types.LambdaType)
    assert isinstance((lambda x, y=42: x), types.LambdaType)
    assert isinstance((lambda x=42, y=43: x), types.LambdaType)
    assert isinstance((lambda x, y=42, z=43: x), types.LambdaType)
    assert isinstance((lambda *args: 1), types.L
