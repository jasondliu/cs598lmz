import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class C(object):
    def f(self):
        pass
assert isinstance(C.f, types.MethodType)
assert type(C.f) is types.MethodType

# Test types.UnboundMethodType
assert isinstance(C.f.__get__(None, C), types.UnboundMethodType)
assert type(C.f.__get__(None, C)) is types.UnboundMethodType

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert type((lambda: None)) is types.LambdaType

# Test types.GeneratorType
def g():
    yield None
assert isinstance(g(), types.GeneratorType)
assert type(g()) is types.
