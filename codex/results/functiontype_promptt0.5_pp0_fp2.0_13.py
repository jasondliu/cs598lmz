import types
# Test types.FunctionType
def test(x):
    return x

assert types.FunctionType == type(test)

# Test types.BuiltinFunctionType
assert types.BuiltinFunctionType == type(len)

# Test types.MethodType
assert types.MethodType == type(test.__call__)

# Test types.UnboundMethodType
assert types.UnboundMethodType == type(test.__call__.__get__(None, test.__class__))

# Test types.LambdaType
assert types.LambdaType == type(lambda: None)

# Test types.GeneratorType
assert types.GeneratorType == type((lambda: (yield))())

# Test types.CodeType
assert types.CodeType == type(test.__code__)

# Test types.TracebackType
try:
    raise Exception
except:
    e, m, tb = sys.exc_info()
    assert types.TracebackType == type(tb)

# Test types.FrameType
assert types.FrameType == type(tb.tb_frame
