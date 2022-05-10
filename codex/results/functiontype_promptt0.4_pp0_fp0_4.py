import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f,types.FunctionType)
assert not isinstance(f,types.BuiltinFunctionType)
assert not isinstance(f,types.BuiltinMethodType)
assert not isinstance(f,types.MethodType)
assert not isinstance(f,types.LambdaType)

def g():
    def h():
        pass
    return h

assert isinstance(g(),types.FunctionType)
assert not isinstance(g(),types.BuiltinFunctionType)
assert not isinstance(g(),types.BuiltinMethodType)
assert not isinstance(g(),types.MethodType)
assert not isinstance(g(),types.LambdaType)

# Test types.BuiltinFunctionType

assert isinstance(len,types.BuiltinFunctionType)
assert not isinstance(len,types.FunctionType)
assert not isinstance(len,types.BuiltinMethodType)
assert not isinstance(len,types.MethodType)
assert not isinstance(len,types.LambdaType)

assert isinstance(len
