import types
# Test types.FunctionType and types.MethodType
def f():
    pass

def g():
    pass

class C:
    def m(self):
        pass

print(type(f))
print(type(g))
print(type(C.m))
print(type(C().m))

print(isinstance(f, types.FunctionType))
print(isinstance(g, types.FunctionType))
print(isinstance(C.m, types.FunctionType))
print(isinstance(C().m, types.FunctionType))

print(isinstance(f, types.MethodType))
print(isinstance(g, types.MethodType))
print(isinstance(C.m, types.MethodType))
print(isinstance(C().m, types.MethodType))

# Test types.BuiltinFunctionType and types.BuiltinMethodType
print(type(len))
print(type([].append))
print(type(C.m.__func__))
print(type(C().m.__func__))

print(isinstance(len, types.BuiltinFunctionType
