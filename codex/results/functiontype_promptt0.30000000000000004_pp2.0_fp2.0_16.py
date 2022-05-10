import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
def f():
    yield 1
g = f()
assert isinstance(g, types.GeneratorType)
# Test types.CodeType
def f():
    pass
assert isinstance(f.__code__, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
def f():
    g()
def g():
    assert isinstance(sys._getframe(), types.FrameType)
f()
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
