import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)

# Test types.MethodType
def m(self):
    pass
assert isinstance(m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(list.append, types.UnboundMethodType)

# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    assert isinstance(e.__traceback__, types.TracebackType)

# Test types.CodeType
def func():
    pass
assert isinstance(func.__code__, types.
