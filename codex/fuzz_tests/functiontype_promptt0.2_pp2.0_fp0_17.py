import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(int) is types.BuiltinFunctionType
assert type(list) is types.BuiltinFunctionType
assert type(dict) is types.BuiltinFunctionType
assert type(open) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(min) is types.BuiltinFunctionType
assert type(max) is types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
assert type(ord) is types.BuiltinFunctionType
assert type(chr) is types.BuiltinFunctionType
assert type(bin) is types.BuiltinFunctionType
assert type(hex) is types.BuiltinFunctionType
assert type(oct) is types.BuiltinFunctionType
assert type(round) is types.BuiltinFunctionType
assert type(divmod) is types.BuiltinFunctionType
assert type(pow) is types.BuiltinFunctionType
assert type(sum) is types.BuiltinFunctionType
