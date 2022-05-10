import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: 1, types.FunctionType)

# Test types.LambdaType
def g():
    return lambda: 1
assert isinstance(g(), types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1
assert isinstance(h(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(h.__code__, types.CodeType)

# Test types.MethodType
class C:
    @staticmethod
    def f():
        pass

assert isinstance(C.f, types.MethodType)

# Test types.UnboundMethodType
class C:
    def f():
        pass

assert isinstance(C.f, types.UnboundMethodType)

# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType
