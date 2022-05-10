import types
# Test types.FunctionType
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# Test types.LambdaType
# print(type(lambda x: x)==types.FunctionType)

# Test types.GeneratorType
# print(type((x for x in range(10)))==types.FunctionType)

# Test types.BuiltinFunctionType
# print(type(abs)==types.FunctionType)

# Test types.UnboundMethodType
# print(type(str.lower)==types.UnboundMethodType)

# Test types.MethodType
# print(type(str.lower)==types.MethodType)

# Test types.BuiltinMethodType
# print(type(str.lower)==types.BuiltinMethodType)

# Test types.ModuleType
# print(type(sys)==types.ModuleType)

# Test types.TracebackType
# print(type(sys.exc_
