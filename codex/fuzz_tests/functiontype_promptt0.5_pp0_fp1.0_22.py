import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass
c = C()
assert isinstance(c.m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
frame = sys._
