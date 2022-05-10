import types
# Test types.FunctionType
print(type(my_function) == types.FunctionType)
print(type(lambda x: x) == types.FunctionType)
# Test types.LambdaType
print(type(lambda x: x) == types.LambdaType)
print(type(my_function) == types.LambdaType)

# Test types.BuiltinFunctionType
print(type(my_function) == types.BuiltinFunctionType)
print(type(min) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(str.join) == types.BuiltinMethodType)
print(type(list.append) == types.BuiltinMethodType)
print(type(my_function) == types.BuiltinMethodType)

# Test types.MethodType
print(type(my_function.__call__) == types.MethodType)
print(type(my_function.__str__) == types.MethodType)
print(type(my_function.__code__) == types.MethodType)
print(type(list.append.__call__
