import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(1, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
# Test types.MethodType
class A:
    def foo(self):
        pass

assert isinstance(A.foo, types.MethodType)
assert not isinstance(f, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(A.foo.__func__, types.UnboundMethodType)
assert not isinstance(f, types.UnboundMethodType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.LambdaType)
# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
# Test types.Gener
