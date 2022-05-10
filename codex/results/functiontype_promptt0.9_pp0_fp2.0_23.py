import types
# Test types.FunctionType

# __main__
def func():
    pass

types.FunctionType

f = func()
# f = None

print isinstance(func, types.FunctionType)

print isinstance(f, types.FunctionType)
