import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda: None

assert type(g) is types.LambdaType
# Test types.GeneratorType
def h():
    yield

assert type(h()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]

assert type(tb) is types.TracebackType
# Test types.FrameType
assert type(tb.tb_frame) is types.FrameType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.ModuleType
assert type(types) is types.ModuleType
# Test types.MethodType
class C:
    def meth(self):
        pass

