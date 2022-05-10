import types
# Test types.FunctionType
def foo(): pass
assert type(foo) is types.FunctionType
assert type(foo) is not types.BuiltinFunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) is not types.FunctionType

# Test types.MethodType
assert type(foo.__call__) is types.MethodType
assert type(foo.__call__) is not types.FunctionType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType
assert type(lambda x: x) is not types.FunctionType

# Test types.GeneratorType
assert type(iter([])) is types.GeneratorType
assert type(iter([])) is not types.FunctionType

# Test types.CodeType
assert type(foo.__code__) is types.CodeType

# Test types.TracebackType
import sys
try:
    1/0
except:
    e, tb, f = sys.exc_info()
assert type(tb) is types.Tr
