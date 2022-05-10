import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
# The name 'int' is a builtin function type, but in the builtins
# module it's a type.  So use a different example.
assert isinstance(len, types.BuiltinFunctionType)
assert type(len) is types.BuiltinFunctionType

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert type(l) is types.LambdaType

# Test types.GeneratorType
g = (i for i in range(10))
assert isinstance(g, types.GeneratorType)
assert type(g) is types.GeneratorType

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.
