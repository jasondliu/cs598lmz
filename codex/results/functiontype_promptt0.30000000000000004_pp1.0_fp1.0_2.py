import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(map, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(map, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert isinstance(map, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(map, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)

# Test types.TracebackType
def f():
    try:
        raise Exception
    except:
        import sys
        return sys.exc_info()[2]

tb = f()
assert isinstance(tb, types.Traceback
