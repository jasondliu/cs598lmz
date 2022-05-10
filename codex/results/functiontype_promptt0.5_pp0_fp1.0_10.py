import types
# Test types.FunctionType
def f1(x):
    return x
assert isinstance(f1, types.FunctionType)
assert isinstance(f1, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.FunctionType)
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
def f2(self):
    return self
class C:
    pass
c = C()
c.f2 = f2
assert isinstance(c.f2, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f2, types.UnboundMethodType)

# Test types.LambdaType
f3 = lambda x: x
assert isinstance(f3, types.LambdaType)

# Test types.GeneratorType
def f4():
    yield None
assert isinstance(f4(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f1.__code__, types.CodeType)

# Test types.Traceback
