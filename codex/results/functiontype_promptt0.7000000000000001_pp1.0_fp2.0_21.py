import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.LambdaType
f = lambda : None
assert type(f) is types.LambdaType
# Test types.GeneratorType
def f(): yield 0
assert type(f) is types.GeneratorType
f = (x for x in [0])
assert type(f) is types.GeneratorType
# Test types.ModuleType
assert type(types) is types.ModuleType
assert type(types) is types.ModuleType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(list) is types.BuiltinFunctionType
assert type(object) is types.BuiltinFunctionType
assert type(object()) is types.BuiltinFunctionType
assert type(tuple) is types.BuiltinFunctionType
assert type(type) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
assert type(dict.fromkeys) is types.BuiltinMethodType
assert type(int.
