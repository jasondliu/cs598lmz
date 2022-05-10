import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
# Test types.TracebackType
tb = None
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
assert isinstance(tb, types.TracebackType)
# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)
# Test types.GeneratorType
assert isinstance((lambda: (yield))(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance((lambda: (yield)).__code__, types.CodeType)
assert isinstance(sys._getframe().f_code, types.CodeType)
# Test types.TypeType
assert isinstance(int, types.TypeType)
assert isinstance(int(), types.TypeType)
assert isinstance(type, types.TypeType)

