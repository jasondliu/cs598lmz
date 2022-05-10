import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert type(f) is not types.BuiltinFunctionType

def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert type(f) is not types.BuiltinFunctionType

def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert type(f) is not types.BuiltinFunctionType

def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert type(f) is not types.BuiltinFunctionType

def f(): pass
assert isinstance(f, types.FunctionType)
assert type(f) is types.Function
