import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
assert type(f) == type(lambda: None)
assert type(f) == type(type)
assert type(f) != type
assert type(f) != type(sys)
assert type(f) != type(1)
assert type(f) != type(None)
assert type(f) != type(Ellipsis)
assert type(f) != type(f())
assert type(f) != type(iter([]))
assert type(f) != type(iter(()))
assert type(f) != type(x for x in range(4))
assert type(f) != type(Exception())
assert type(f) != type(Exception)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert type(max) == types.BuiltinFunctionType
assert type(min) == types.BuiltinFunctionType
assert type(ord) == types
