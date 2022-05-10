import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda: 0, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.FrameType
assert isinstance(f.__code__.co_frame, types.FrameType)
# Test types.GetSetDescriptorType
class C:
    def __get__(self, obj, type=None):
        return 1

assert isinstance(C(), types.GetSetDescriptorType)
# Test types.MemberDescriptorType
class C:
