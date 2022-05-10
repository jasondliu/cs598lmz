import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert type(C.m) == types.MethodType
assert isinstance(C.m, types.MethodType)

# Test types.UnboundMethodType
assert type(C.m) == types.MethodType
assert isinstance(C.m, types.MethodType)

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert type(g()) == types.GeneratorType
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert type(f.
