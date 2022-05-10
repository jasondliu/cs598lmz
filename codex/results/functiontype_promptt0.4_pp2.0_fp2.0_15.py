import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(f) is types.FunctionType
assert type(int) is types.BuiltinFunctionType
assert type(list) is types.BuiltinFunctionType
assert type(dict) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(compile) is types.BuiltinFunctionType
assert type(iter) is types.BuiltinFunctionType
assert type(map) is types.BuiltinFunctionType
assert type(filter) is types.BuiltinFunctionType
assert type(range) is types.BuiltinFunctionType
assert type(sorted) is types.BuiltinFunctionType
assert type(__import__) is types.BuiltinFunctionType
assert type(vars) is types.BuiltinFunctionType
assert type(dir) is types.BuiltinFunctionType
assert type(divmod) is types.BuiltinFunctionType
assert type(hash) is types.BuiltinFunctionType
assert type(hex) is types.BuiltinFunctionType

