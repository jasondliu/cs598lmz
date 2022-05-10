import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert types.FunctionType is type(f)
# Test types.BuiltinFunctionType
assert type(int) is types.BuiltinFunctionType
assert types.BuiltinFunctionType is type(int)
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) is types.MethodType
assert types.MethodType is type(A.f)
assert type(A().f) is types.MethodType
assert types.MethodType is type(A().f)
# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType
assert types.UnboundMethodType is type(A.f)
assert type(A().f) is types.MethodType
assert types.MethodType is type(A().f)
# Test types.LambdaType
a = lambda: None
assert type(a) is types.LambdaType
assert types.LambdaType is type(a)
# Test types.GeneratorType
def f():
