import types
# Test types.FunctionType,
# types.TypeType and
# types.LambdaType.
def func():
    pass

class A:
    pass

def test_functiontype():
    assert type(func) == types.FunctionType
    raises(TypeError, func, 'foo')

def test_type():
    assert type(A) == types.TypeType
    assert type(A()) == A

def test_lambdatype():
    assert type(lambda: 42) == types.LambdaType

# XXX check that type(X) == types.ClassType
