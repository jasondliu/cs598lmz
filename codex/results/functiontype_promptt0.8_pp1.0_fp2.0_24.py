import types
# Test types.FunctionType()
def test():
    return 1
print(type(test))
print(types.FunctionType is type(test))
