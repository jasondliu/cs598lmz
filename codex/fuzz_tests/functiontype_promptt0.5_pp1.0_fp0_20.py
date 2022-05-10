import types
# Test types.FunctionType
def foo(): pass
assert type(foo) is types.FunctionType
# Test types.LambdaType
bar = lambda x: x
assert type(bar) is types.LambdaType
# Test types.GeneratorType
def baz():
    yield 1
    yield 2
    yield 3
assert type(baz()) is types.GeneratorType
# Test types.BuiltinFunctionType
assert type(print) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.UnboundMethodType
assert type(list.append) is types.UnboundMethodType
# Test types.MethodType
assert type([].append) is types.MethodType

# Test types.CodeType
def qux(): pass
assert type(qux.__code__) is types.CodeType

# Test types.FrameType
assert type(sys._getframe()) is types.FrameType

# Test types.TracebackType
try:
    1 / 0
except:
    assert type(sys.exc_info()
