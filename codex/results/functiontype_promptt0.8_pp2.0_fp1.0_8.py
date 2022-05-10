import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert type(map) == types.BuiltinFunctionType
assert isinstance(map, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def m(self): pass
assert type(A().m) == types.MethodType
assert isinstance(A().m, types.MethodType)

# Test types.UnboundMethodType
assert type(A.m) == types.UnboundMethodType
assert isinstance(A.m, types.UnboundMethodType)

# Test types.LambdaType
assert type((lambda x:x)) == types.LambdaType
assert isinstance((lambda x:x), types.LambdaType)

# Test types.GeneratorType
assert type((x for x in range(2))) == types.GeneratorType
assert isinstance((x for x in range(2)), types.GeneratorType)

# Test types.CodeType
assert type(f
