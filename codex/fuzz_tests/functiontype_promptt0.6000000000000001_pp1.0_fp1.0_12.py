import types
# Test types.FunctionType
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(max, types.BuiltinFunctionType)
# Test types.ModuleType
import types
assert isinstance(types, types.ModuleType)
# Test types.TypeType
assert isinstance(int, types.TypeType)
# Test types.UnboundMethodType
assert isinstance(f.__call__, types.UnboundMethodType)
# Test types.MethodType
assert isinstance(f.__call__.__get__(f), types.MethodType)
# Test types.LambdaType
assert isinstance(lambda x: 1, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in []), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.FrameType

