import types
# Test types.FunctionType
assert issubclass(types.FunctionType, object)
@nottest
def f():
    pass
assert type(f) is types.FunctionType
# Test types.BuiltinFunctionType
assert issubclass(types.BuiltinFunctionType, object)
# XXX Add method to test types.BuiltinFunctionType (using type(int))
# Test types.MethodType
assert issubclass(types.MethodType, object)
assert type(str.upper) is types.MethodType
# Test types.UnboundMethodType
assert issubclass(types.UnboundMethodType, object)
assert type(str.upper) is not types.UnboundMethodType
assert type(str.upper) is types.MethodType
# Test types.TracebackType
assert issubclass(types.TracebackType, object)
#XXX Add method to test types.TracebackType
# Test types.FrameType
assert issubclass(types.FrameType, object)
#XXX Add method to test types.FrameType
# Test types.CodeType
assert issubclass(types.CodeType, object)
#XXX
