import types
# Test types.FunctionType

class A:
    pass

def f():
    pass

a = A()

print(isinstance(f, types.FunctionType))
print(isinstance(a, types.FunctionType))
print(isinstance(A, types.FunctionType))

print(type(f) == types.FunctionType)
print(type(a) == types.FunctionType)
print(type(A) == types.FunctionType)

print(type(f) is types.FunctionType)
print(type(a) is types.FunctionType)
print(type(A) is types.FunctionType)

print(type(f) is types.BuiltinFunctionType)
print(type(a) is types.BuiltinFunctionType)
print(type(A) is types.BuiltinFunctionType)

print(type(f) is types.BuiltinMethodType)
print(type(a) is types.BuiltinMethodType)
print(type(A) is types.BuiltinMethodType)

print(type(f) is types.MethodType)
print(type(a)
