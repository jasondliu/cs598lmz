import types
# Test types.FunctionType
def f1():
    pass

print(isinstance(f1, types.FunctionType))
print(isinstance(f1, types.BuiltinFunctionType))

print(isinstance(len, types.BuiltinFunctionType))
