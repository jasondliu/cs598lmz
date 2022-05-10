import types
# Test types.FunctionType
def f(x):
    return x

assert isinstance(f, types.FunctionType)
assert issubclass(type(f), types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert issubclass(type(len), types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance("abc".find, types.BuiltinMethodType)
assert issubclass(type("abc".find), types.BuiltinMethodType)
# Test types.MethodType
class A:
    def f(self, x):
        return x

a = A()
assert isinstance(a.f, types.MethodType)
assert issubclass(type(a.f), types.MethodType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert issubclass(type(lambda x: x), types.LambdaType)
