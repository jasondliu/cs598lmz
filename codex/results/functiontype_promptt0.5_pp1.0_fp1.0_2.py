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
assert isinstance(list, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)

# Test types.ModuleType
# TODO: this is not true for micropython
#assert isinstance(types, types.ModuleType)

# Test types.TypeType
# TODO: this is not true for micropython
#assert isinstance(type, types.TypeType)

# Test types.TracebackType
# TODO: this is not true for micropython
#try:
#    raise Exception
#except Exception:
#    e = sys.exc_info()[2]
#    assert
