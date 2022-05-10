import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.MethodType
class C(object):
    def f(self):
        pass
assert type(C().f) is types.MethodType

# Test types.UnboundMethodType
assert type(C.f) is types.UnboundMethodType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(10))) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) is types.TracebackType

# Test types.FrameType
def g():
    assert type(sys._getframe()) is types.FrameType
g()

# Test types
