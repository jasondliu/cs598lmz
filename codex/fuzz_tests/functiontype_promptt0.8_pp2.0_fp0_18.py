import types
# Test types.FunctionType

def fun():
    pass

print(fun, type(fun))
print(isinstance(fun, types.FunctionType))
print(isinstance(list, types.FunctionType))
