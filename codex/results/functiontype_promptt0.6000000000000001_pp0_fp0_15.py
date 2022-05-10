import types
# Test types.FunctionType and types.BuiltinFunctionType

class C:
    def f(self):
        pass

def g():
    pass

print(type(g) is types.FunctionType)
print(type(C.f) is types.MethodType)
print(type(C().f) is types.MethodType)
print(type(C.f) is types.FunctionType)
print(type(C().f) is types.FunctionType)
print(type(lambda: 1) is types.FunctionType)
print(type(type(1)) is types.FunctionType)

print(type(abs) is types.BuiltinFunctionType)
print(type(C.f) is types.BuiltinFunctionType)
print(type(C().f) is types.BuiltinFunctionType)
print(type(g) is types.BuiltinFunctionType)
print(type(lambda: 1) is types.BuiltinFunctionType)
print(type(type(1)) is types.BuiltinFunctionType)

# Test types.ClassType

class C:
    def f(self):
       
