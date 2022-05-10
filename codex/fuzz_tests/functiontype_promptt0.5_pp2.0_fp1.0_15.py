import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(lambda: None, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)

# Test types.GeneratorType
def f():
    yield 1

assert isinstance(f(), types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance("".find, types.BuiltinMethodType)
assert not isinstance(abs, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C().f, types.MethodType)
assert not isinstance(f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f,
