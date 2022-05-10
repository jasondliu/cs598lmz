import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.LambdaType
f = lambda x: x
assert type(f) is types.LambdaType
# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.FrameType
def h():
    assert type(sys._getframe()) is types.FrameType
h()
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.ModuleType
assert type(types) is types.ModuleType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.MethodType
class C:
    def f(self): pass

