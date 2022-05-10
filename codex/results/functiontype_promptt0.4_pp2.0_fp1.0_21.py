import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType
assert type(f) is types.BuiltinMethodType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType
assert type(g) is types.FunctionType
assert type(g) is types.BuiltinFunctionType
assert type(g) is types.BuiltinMethodType
assert type(g) is types.MethodType
assert type(g) is types.BuiltinMethodType

# Test types.GeneratorType
def gen():
    yield 1
h = gen()
assert type(h) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(g.__code__) is types.CodeType
assert type(gen.__code__) is types.CodeType

# Test types.TracebackType
import
