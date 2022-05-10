import types
# Test types.FunctionType works
def f(x, y):
    return x + y
b = types.FunctionType(f.__code__, {})
print(b(2, 3))
