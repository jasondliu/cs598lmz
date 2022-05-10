import types
# Test types.FunctionType

assert isinstance(lambda x: x, types.FunctionType)
assert type(lambda x: x) is types.FunctionType
assert hasattr(types.FunctionType, '__module__')
assert hasattr(types.FunctionType, '__qualname__')

assert not isinstance(lambda x: x, types.LambdaType)
assert type(lambda x: x) is not types.LambdaType

assert not isinstance(lambda x: x, types.GeneratorType)
assert type(lambda x: x) is not types.GeneratorType

try:
    class A:
        def __init__(self, x):
            self.x = x
        def __call__(self, y):
            return 2 * self.x * y
    f = A(3)
    assert not isinstance(f, types.FunctionType)
    assert type(f) is not types.FunctionType
except:
    print("SKIP")
    raise SystemExit

# Test types.BuiltinFunctionType

import builtins

assert isinstance(max, types.Built
