from types import FunctionType
a = (x for x in [1])
def func():
    return 1
print type(a)
print type(func)

print FunctionType

print isinstance(func, FunctionType)
print isinstance(a, FunctionType)

print isinstance(func, types.FunctionType)
print isinstance(a, types.FunctionType)

print type(lambda:1)
print isinstance(lambda:1, types.FunctionType)

print isinstance(lambda:1, FunctionType)
print isinstance(lambda:1, types.BuiltinFunctionType)


print isinstance(func, types.BuiltinFunctionType)
print isinstance(a, types.BuiltinFunctionType)
