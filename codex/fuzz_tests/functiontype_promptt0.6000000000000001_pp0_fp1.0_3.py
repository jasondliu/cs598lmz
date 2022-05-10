import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.MethodType
class A(object):
    def f(self): pass
assert isinstance(A.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f.__get__(object()), types.MethodType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)

# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)

# Test types.TracebackType
try:
    1/0
except Exception:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
import inspect
assert isinstance(inspect.currentframe(), types.FrameType)

# Test types.SliceType
assert isinstance(slice(1,2), types.SliceType)


