import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type(str.upper) is types.BuiltinMethodType

# Test types.MethodType
class A:
    def m(self): pass
assert type(A().m) is types.MethodType

# Test types.UnboundMethodType
assert type(A.m) is types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((i for i in range(10))) is types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    assert type(e.__traceback__) is types.TracebackType

# Test types.FrameType
def f():
    assert type(f.__code
