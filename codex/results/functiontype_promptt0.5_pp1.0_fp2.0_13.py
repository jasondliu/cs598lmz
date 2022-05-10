import types
# Test types.FunctionType
def f(x):
    return x

print(type(f))
print(type(f(1)))

print(isinstance(f, types.FunctionType))
print(isinstance(f(1), types.FunctionType))

print(types.FunctionType)

# Test types.LambdaType
g = lambda x: x

print(type(g))
print(type(g(1)))

print(isinstance(g, types.LambdaType))
print(isinstance(g(1), types.LambdaType))

print(types.LambdaType)

# Test types.MethodType
class C:
    def f(self):
        return 1

print(type(C.f))
print(type(C().f))

print(isinstance(C.f, types.MethodType))
print(isinstance(C().f, types.MethodType))

print(types.MethodType)

# Test types.BuiltinFunctionType
def f(x):
    return x

print(type(f))
print
