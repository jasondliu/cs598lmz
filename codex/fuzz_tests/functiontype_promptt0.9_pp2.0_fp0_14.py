import types
# Test types.FunctionType
from types import FunctionType
test_class = types.FunctionType('foo', 1, 2, 3)
test_class
test_class.__call__()
# Test types.BuiltinFunctionType
def test_function():
    pass
test_function = types.BuiltinFunctionType(test_function, 1000, 2, 3)
test_function
test_function = types.BuiltinFunctionType(test_function)
test_function
test_function = types.BuiltinFunctionType(test_function)
test_function
test_function = types.BuiltinFunctionType(test_function)
test_function
test_function = types.BuiltinFunctionType(test_function)
test_function
# Test types.MethodType
class foo:
    def __init__(self):
        pass
    pass
test_class = types.MethodType('foo', foo)
test_class
test_class2 = types.MethodType('foo', foo, types.BuiltinFunctionType(foo))
test_class2
# Test types.BuiltinMethodType
def foo(self):
    pass
test_
