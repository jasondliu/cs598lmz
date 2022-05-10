import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.MethodType
assert type(f.__call__) is types.MethodType
# Test types.BuiltinMethodType
assert type(len.__call__) is types.BuiltinMethodType
# Test types.UnboundMethodType
assert type(f.__call__.__get__) is types.UnboundMethodType
# Test types.ClassType
class C:
    def f(self):
        pass
assert type(C) is types.ClassType
# Test types.TypeType
assert type(C) is types.TypeType
# Test types.InstanceType
assert type(C()) is types.InstanceType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType
# Test types.CodeType
assert type(f.func_code) is types.CodeType
