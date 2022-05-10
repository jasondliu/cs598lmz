import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)
# Test types.FrameType
def h():
    assert isinstance(sys._getframe(), types.FrameType)
h()
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.ClassType
class C:
    pass
assert isinstance(C, types.ClassType)
# Test types.InstanceType
assert isinstance(C(), types.InstanceType)
# Test types.MethodType
assert is
