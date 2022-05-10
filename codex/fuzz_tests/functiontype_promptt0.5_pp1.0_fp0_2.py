import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda x: x
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1
    yield 2
h = gen()
assert isinstance(h, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)
assert isinstance(g.func_code, types.CodeType)
assert isinstance(h.gi_code, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(tb.tb_frame, types.FrameType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert
