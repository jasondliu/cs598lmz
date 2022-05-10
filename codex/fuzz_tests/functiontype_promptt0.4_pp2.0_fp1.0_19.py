import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.FrameType
def f():
    assert type(sys._getframe()) == types.FrameType
f()
# Test types.TracebackType
try:
    1/0
except:
    assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.GetSetDescriptorType
assert type(type.__dict__['__dict__']) == types.GetSetDescriptorType
# Test types.MemberDescriptorType
assert type(type.__dict__['__doc__']) == types.MemberDescriptorType
# Test types.Wra
