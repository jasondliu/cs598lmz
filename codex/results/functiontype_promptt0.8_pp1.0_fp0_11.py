import types
# Test types.FunctionType and types.LambdaType

def func(a, b, c): return a + b + c

try:
    a = types.FunctionType
except AttributeError:
    raise TestSkipped, "types.FunctionType not available on this build"
else:
    if type(a) != type(func):
        raise TestFailed, "types.FunctionType is not correct"
    if type(a) != type(func.__class__):
        raise TestFailed, "types.FunctionType is not correct"
    if not isinstance(func, a):
        raise TestFailed, "func is not an instance of types.FunctionType"

try:
    a = types.LambdaType
except AttributeError:
    raise TestSkipped, "types.LambdaType not available on this build"
else:
    if type(a) != type(lambda x, y: x + y):
        raise TestFailed, "types.LambdaType is not correct"
    if type(a) != type((lambda x, y: x + y).__class__
