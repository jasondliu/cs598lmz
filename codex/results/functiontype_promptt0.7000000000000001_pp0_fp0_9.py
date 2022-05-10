import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)

# Test override existing name with a class and a lambda
class _C:
    def __init__(self, x):
        pass

_C = lambda: None

# Test that lambda can't be used as a base class
try:
    class C(lambda: None):
        pass
except TypeError as e:
    assert "argument of type 'lambda'" in str(e)

# Test that lambda can't be used as a metaclass
try:
    class C(metaclass=lambda: None):
        pass
except TypeError as e:
    assert "argument of type 'lambda'" in str(e)

# Test that lambda can't be used as a decorator
try:
    @lambda: None
    def f():
        pass
except TypeError as e:
    assert "argument of type 'lambda'" in str(e)

# Test that lambda can't be used as a return type
