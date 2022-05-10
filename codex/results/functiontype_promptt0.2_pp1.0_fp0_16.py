import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, types.FunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.FunctionType)

# Test types.UnboundMethodType
assert isinstance(A.f.__func__, types.UnboundMethodType)
assert isinstance(A.f.__func__, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)
assert isinstance((lambda x: x), types.FunctionType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(
