import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(map, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(lambda x: x, types.CodeType)
# Test types.TracebackType
try:
    raise Exception()
except Exception as e:
    assert isinstance(e.__traceback__, types.TracebackType)
# Test types.FrameType
try:
    raise Exception()
except Exception as e:
    assert isinstance(e.__traceback__.tb_frame, types.FrameType)
# Test types.GetSetDescriptorType
assert isinstance(int.numerator, types.GetSetDescriptorType)
# Test types.MemberDescriptorType
assert isinstance(int.numerator, types.Member
