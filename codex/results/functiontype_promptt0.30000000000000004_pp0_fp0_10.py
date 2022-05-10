import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def m(self):
        pass

assert isinstance(A.m, types.MethodType)
assert isinstance(A.m, types.BuiltinMethodType)

# Test types.UnboundMethodType
assert isinstance(A.m.__func__, types.UnboundMethodType)
assert isinstance(A.m.__func__, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(A.m.__func__, types.BuiltinFunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert isinstance(l, types.FunctionType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(
