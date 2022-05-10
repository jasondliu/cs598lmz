import types
# Test types.FunctionType
def f():
    pass

assert(isinstance(f, types.FunctionType))

# Test types.LambdaType
g = lambda x: x

assert(isinstance(g, types.LambdaType))

# Test types.CodeType
assert(isinstance(f.__code__, types.CodeType))

# Test types.FrameType
def h():
    assert(isinstance(h.__code__.__code__.co_frame, types.FrameType))

h()

# Test types.TracebackType
def i():
    raise Exception

try:
    i()
except Exception as e:
    assert(isinstance(e.__traceback__, types.TracebackType))

# Test types.ModuleType
assert(isinstance(types, types.ModuleType))

# Test types.BuiltinFunctionType
assert(isinstance(len, types.BuiltinFunctionType))

# Test types.BuiltinMethodType
assert(isinstance(len, types.BuiltinFunctionType))

# Test types.MethodType
assert
