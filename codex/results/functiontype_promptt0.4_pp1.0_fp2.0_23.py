import types
# Test types.FunctionType

def f(): pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType
assert type(lambda x, y: x) is types.FunctionType
assert type(lambda x, y=1: x) is types.FunctionType
assert type(lambda x, y=1, *args: x) is types.FunctionType
assert type(lambda x, y=1, *args, **kw: x) is types.FunctionType
assert type(lambda x, y=1, *, z=2, **kw: x) is types.FunctionType

# Test types.LambdaType

def f(): pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType
assert type(lambda x, y: x) is types.FunctionType
assert type(lambda x, y=1: x) is types.FunctionType
assert type(lambda x, y=1, *args: x) is
