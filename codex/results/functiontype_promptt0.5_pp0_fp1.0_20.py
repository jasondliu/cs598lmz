import types
# Test types.FunctionType to see if it is a function
print(type(abs)==types.FunctionType)
# Test types.LambdaType to see if it is a lambda function
print(type(lambda x: x)==types.LambdaType)
# Test types.GeneratorType to see if it is a generator function
print(type((x for x in range(10)))==types.GeneratorType)

# Test types.BuiltinFunctionType to see if it is a built-in function
print(type(abs)==types.BuiltinFunctionType)
# Test types.BuiltinMethodType to see if it is a built-in method
print(type([].append)==types.BuiltinMethodType)
# Test types.MethodType to see if it is a method
print(type('abc'.lower)==types.MethodType)

# Test types.ModuleType to see if it is a module
print(type(types)==types.ModuleType)
# Test types.TypeType to see if it is a type
print(type(type)==types.TypeType)

# Test types.ClassType to see
