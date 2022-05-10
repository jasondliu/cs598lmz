import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, types.FunctionType)

# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.FunctionType)

# Test types.UnboundMethodType
assert isinstance(A.f.__get__(None, A), types.UnboundMethodType)
assert isinstance(A.f.__get__(None, A), types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert isinstance((lambda: None), types.FunctionType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__
