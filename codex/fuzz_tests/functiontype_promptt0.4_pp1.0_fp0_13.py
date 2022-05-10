import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance(None, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(pow, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.LambdaType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert not isinstance(f, types.CodeType)

# Test types.TracebackType
import sys
assert isinstance(sys.exc_info()[2], types.Traceback
