import types
# Test types.FunctionType
def f():
    pass

print(type(f) is types.FunctionType)
print(type(lambda: None) is types.FunctionType)
print(type(lambda x: x) is types.FunctionType)
print(type(lambda x, y: x + y) is types.FunctionType)
print(type(lambda *args: None) is types.FunctionType)
print(type(lambda **kwargs: None) is types.FunctionType)
print(type(lambda *args, **kwargs: None) is types.FunctionType)

# Test types.LambdaType
print(type(lambda: None) is types.LambdaType)
print(type(lambda x: x) is types.LambdaType)
print(type(lambda x, y: x + y) is types.LambdaType)
print(type(lambda *args: None) is types.LambdaType)
print(type(lambda **kwargs: None) is types.LambdaType)
print(type(lambda *args, **kwargs: None) is types.Lambda
