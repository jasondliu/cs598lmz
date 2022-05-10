import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.LambdaType
g = lambda x: x

assert isinstance(g, types.LambdaType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)

# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)

# Test types.ModuleType
import types
assert isinstance(types, types.ModuleType)

# Test types.TypeType
assert isinstance(int, types.TypeType)
assert not isinstance(1, types.TypeType)

# Test types.UnboundMethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.UnboundMethodType)
assert not isinstance(C.f, types.MethodType)
assert not isinstance(C().f, types.UnboundMethodType)

