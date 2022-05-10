import types
# Test types.FunctionType
a = lambda: 1
b = lambda: 1
print(type(a) == types.FunctionType)
print(type(b) == type(a))

# Test types.LambdaType
a = lambda: 1
b = lambda: 1
print(type(a) == types.LambdaType)
print(type(b) == type(a))
