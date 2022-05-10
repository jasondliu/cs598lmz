import types
# Test types.FunctionType
f = lambda x: x
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
def f():
    yield 0
assert isinstance(f(), types.GeneratorType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
    assert tb.tb_next is None
# Test types.FrameType
def f():
    g()
def g():
    return sys._getframe()
assert isinstance(f(), types.FrameType)
# Test types.CodeType
def f(): pass
assert isinstance(f.func_code, types.CodeType)
# Test types.TypeType
assert isinstance(int, types.TypeType)
# Test types.ClassType
class f(object): pass
assert isinstance(f, types.ClassType)
# Test
