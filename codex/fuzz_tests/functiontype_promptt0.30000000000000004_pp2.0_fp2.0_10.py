import types
# Test types.FunctionType

def f():
    pass

assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

assert issubclass(types.FunctionType, object)
assert issubclass(types.BuiltinFunctionType, object)

assert issubclass(types.FunctionType, types.BuiltinFunctionType)

assert not issubclass(types.BuiltinFunctionType, types.FunctionType)

# Test types.CodeType

def f():
    pass

assert type(f.__code__) is types.CodeType

assert isinstance(f.__code__, types.CodeType)

assert issubclass(types.CodeType, object)

# Test types.FrameType

def f():
    return f.__code__.co_filename

assert type(f.__code__.co_filename) is str

# Test types.TracebackType

try:
    raise Exception
except Exception as
