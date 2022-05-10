import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)

# Test types.ClassType
class D:
    pass

assert isinstance(D, types.ClassType)

# Test types.TypeType
assert isinstance(D, types.TypeType)

# Test types.InstanceType
assert isinstance(D(), types.InstanceType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)


