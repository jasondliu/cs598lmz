import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(lambda: None, types.BuiltinMethodType)
assert isinstance(int.__dict__['__new__'], types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(lambda: None, types.MethodType)
assert isinstance(int.__dict__['__new__'], types.MethodType)
assert not isinstance(f, types.UnboundMethodType)
assert not isinstance(lambda: None, types.UnboundMethodType)
assert isinstance(int.__dict__['__new__'], types.UnboundMethodType)

# Test types.L
