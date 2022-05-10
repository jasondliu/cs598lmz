import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(3, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(3, types.LambdaType)

# Test types.GeneratorType
def f(): yield 1
assert isinstance(f(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(3, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert not isinstance(f, types.CodeType)
assert not isinstance(3, types.CodeType)

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types
