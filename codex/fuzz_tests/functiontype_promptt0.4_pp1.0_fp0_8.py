import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert f.__class__ is types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert len.__class__ is types.BuiltinFunctionType
# Test types.MethodType
class A:
    def m(self): pass
assert type(A.m) is types.MethodType
assert A.m.__class__ is types.MethodType
assert type(A().m) is types.MethodType
assert A().m.__class__ is types.MethodType
# Test types.UnboundMethodType
assert type(A.m) is types.UnboundMethodType
assert A.m.__class__ is types.UnboundMethodType
# Test types.InstanceType
assert type(A()) is types.InstanceType
assert A().__class__ is types.InstanceType
# Test types.LambdaType
assert type(lambda : 0) is types.LambdaType
assert (lambda : 0).__class__ is types.LambdaType
# Test types.Generator
