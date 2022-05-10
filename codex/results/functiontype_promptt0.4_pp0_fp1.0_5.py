import types
# Test types.FunctionType
assert type(lambda x: x) == types.FunctionType
# Test types.GeneratorType
assert type(x for x in range(10)) == types.GeneratorType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType
# Test types.MethodType
assert type([].append) == types.MethodType
# Test types.UnboundMethodType
assert type(list.append) == types.UnboundMethodType
# Test types.ModuleType
assert type(types) == types.ModuleType
# Test types.TracebackType
assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.FrameType
assert type(sys._getframe()) == types.FrameType
# Test types.CodeType
assert type(lambda x: x).__code__ == types.CodeType
# Test types.TypeType
assert type(int) == types.TypeType
# Test types.SliceType
assert type(slice(0))
