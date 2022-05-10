import types
# Test types.FunctionType

def f():
    pass

print(type(f) is types.FunctionType)
print(type(lambda x: x) is types.FunctionType)
print(type(f.__call__) is types.FunctionType)
print(type(f.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__.__call__.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__.__call__.__call__.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__.__call__.__call__.__call__.__call__.__call__) is types.FunctionType)
print(type(f.__call__.__call__
