import types
# Test types.FunctionType
#
print('types.FunctionType')
def f(): pass
print(type(f) is types.FunctionType)

# Test types.BuiltinFunctionType
#
print('types.BuiltinFunctionType')
print(type(len) is types.BuiltinFunctionType)

# Test types.MethodType
#
print('types.MethodType')
class C:
    def f(self): pass
print(type(C.f) is types.MethodType)

# Test types.UnboundMethodType
#
print('types.UnboundMethodType')
print(type(C.f) is types.UnboundMethodType)
print(type(C.f) is not types.MethodType)
print(type(C().f) is types.MethodType)
print(type(C().f) is not types.UnboundMethodType)

# Test types.LambdaType
#
print('types.LambdaType')
print(type(lambda: 1) is types.LambdaType)

# Test types.GeneratorType
#
print('types.Generator
