import types
# Test types.FunctionType
def func():
    pass
if type(func) is types.FunctionType:
    print('FunctionType is ok')

# Test types.LambdaType
f = lambda x:x+1
if type(f) is types.LambdaType:
    print('LambdaType is ok')

# Test types.CodeType
def func():
    pass
if type(func.__code__) is types.CodeType:
    print('CodeType is ok')

# Test types.TracebackType
try:
    raise RuntimeError
except RuntimeError:
    if type(sys.exc_info()[2]) is types.TracebackType:
        print('TracebackType is ok')

# Test types.FrameType
def func():
    return sys._getframe()
if type(func()) is types.FrameType:
    print('FrameType is ok')

# Test types.BuiltinFunctionType
if type(print) is types.BuiltinFunctionType:
    print('BuiltinFunctionType is ok')

# Test types.BuiltinMethodType

