import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(min, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(g().__next__, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def f(self):
        pass
assert isinstance(A().f, types.MethodType)

# Test types.ModuleType
# Note: this is a bit of a hack, but we need to test it somehow
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try:
    1/0
except Exception as e:
    assert isinstance(e.__traceback__, types.TracebackType)

# Test types.FrameType
