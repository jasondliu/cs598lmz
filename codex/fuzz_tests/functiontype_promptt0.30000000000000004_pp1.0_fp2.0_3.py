import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
assert isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(g, types.MethodType)

# Test types.GeneratorType
def gen():
    yield 1
assert isinstance(gen(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(gen.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except Exception as e:
   
