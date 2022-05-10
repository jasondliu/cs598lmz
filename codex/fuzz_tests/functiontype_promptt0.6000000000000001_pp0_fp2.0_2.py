import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.LambdaType
f = lambda: None
assert type(f) is types.LambdaType

# Test types.GeneratorType
def g():
    yield
assert type(g()) is types.GeneratorType

# Test types.MethodType
class C:
    def m(self):
        pass
c = C()
assert type(c.m) is types.MethodType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.ModuleType
assert type(types) is types.ModuleType

# Test types.TracebackType
try:
    raise Exception()
except Exception as e:
    tb = e.__traceback__
assert type(tb) is types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) is types.FrameType
