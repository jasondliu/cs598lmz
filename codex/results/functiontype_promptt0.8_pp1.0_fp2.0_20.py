import types
# Test types.FunctionType is callable and call it.
def f(): pass
assert isinstance(f, types.FunctionType) and callable(f)
assert f() is None
# Test types.LambdaType is callable and call it.
assert isinstance(lambda: None, types.LambdaType) and callable(lambda: None)
assert (lambda: None)() is None
# Test types.ClassType is callable and call it.
assert isinstance(str, types.ClassType) and callable(str)
assert str() == ''
# Test types.MethodType is callable and call it.
assert isinstance('', types.MethodType) and callable('')
assert ''() == ''

# Test types.CodeType.
def g():
    def f():
        pass
    return f.func_code
assert isinstance(g.func_code, types.CodeType)
# Test types.TracebackType
try:
    raise SystemExit
except SystemExit:
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.
