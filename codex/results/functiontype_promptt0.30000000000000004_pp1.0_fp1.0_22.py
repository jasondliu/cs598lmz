import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
# LambdaType is a subclass of FunctionType
print(issubclass(types.LambdaType, types.FunctionType))

# Test types.GeneratorType
# GeneratorType is a subclass of FunctionType
print(issubclass(types.GeneratorType, types.FunctionType))

# Test types.BuiltinFunctionType
# BuiltinFunctionType is a subclass of FunctionType
print(issubclass(types.BuiltinFunctionType, types.FunctionType))

# Test types.BuiltinMethodType
# BuiltinMethodType is a subclass of FunctionType
print(issubclass(types.BuiltinMethodType, types.FunctionType))

# Test types.MethodType
# MethodType is a subclass of FunctionType
print(iss
