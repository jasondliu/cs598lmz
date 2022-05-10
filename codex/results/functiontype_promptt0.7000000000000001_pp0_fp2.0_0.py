import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda : None, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda : None, types.LambdaType)

# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]

assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)

g()

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.GeneratorType
def h():
    yield None

assert isinstance(h(), types.GeneratorType)

# Test types.MemberDescript
