import types
# Test types.FunctionType, types.LambdaType, types.GeneratorType

def f(): pass
def g(): yield 0

print type(f) is types.FunctionType
print type(g) is types.FunctionType
print type(lambda: None) is types.LambdaType
print type(g()) is types.GeneratorType

# Test types.ClassType, types.TypeType

class C: pass

print type(C) is types.ClassType
print type(C()) is types.InstanceType
print type(type) is types.TypeType
print type(types) is types.ModuleType
print type(object) is types.TypeType

# Test types.UnboundMethodType, types.MethodType

class D:
    def meth(self): pass

print type(D.meth) is types.UnboundMethodType
print type(D().meth) is types.MethodType

# Test types.BuiltinFunctionType, types.BuiltinMethodType

print type(len) is types.BuiltinFunctionType
print type([].append) is types.BuiltinMethodType

