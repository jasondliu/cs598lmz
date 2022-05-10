import types
# Test types.FunctionType

def f():
    pass

print(type(f))
print(isinstance(f, types.FunctionType))
