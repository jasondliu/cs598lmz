import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(1, types.LambdaType)

# Test types.GeneratorType
def f(): yield 1
assert isinstance(f(), types.GeneratorType)
assert isinstance((x for x in range(10)), types.GeneratorType)
assert not isinstance(1, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance((lambda: None).__code__, types.CodeType)
assert not isinstance(1, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
