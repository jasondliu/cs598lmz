import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.TracebackType
try:
    1/0
except Exception as e:
    tb = e.__traceback__
assert type(tb) is types.TracebackType

# Test types.GeneratorType
def f():
    yield 1
assert type(f()) is types.GeneratorType

# Test types.CodeType
def f():
    pass
assert type(f.__code__) is types.CodeType

# Test types.FrameType
def f():
    assert type(_) is types.FrameType
f()

# Test types.MethodType
class A:
    def m():
        pass
assert type(A.m) is types.MethodType

# Test types.BuiltinMethodType
assert type(str.replace) is types.BuiltinMethodType
