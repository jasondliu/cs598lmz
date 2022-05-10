import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda x: x
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1
assert isinstance(h(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(h.__code__, types.CodeType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance("".upper, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.Trace
