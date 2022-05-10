import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(lambda: None) == types.FunctionType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
def f():
    yield 1

assert type(f()) == types.GeneratorType
# Test types.GeneratorType
assert type(f()) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.FrameType
assert type(sys._getframe()) == types.FrameType
# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.ModuleType
assert type(types) == types.ModuleType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
# Test types
