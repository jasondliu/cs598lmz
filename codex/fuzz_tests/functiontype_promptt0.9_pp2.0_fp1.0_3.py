import types
# Test types.FunctionType and types.UnboundMethodType
print(type(abs))
print(type(int.__abs__))
# FunctionType and MethodType are all true
print(isinstance(abs, types.FunctionType))
print(isinstance(int.__abs__, types.UnboundMethodType))
print(isinstance(int.__abs__, types.FunctionType))
print(isinstance(int.__abs__, types.BuiltinFunctionType))
print(int.__abs__)
