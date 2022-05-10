import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.ClassType
class C:
    pass
assert type(C) is types.ClassType

# Test types.TypeType
assert type(C) is types.TypeType
assert type(type) is types.TypeType

# Test types.UnboundMethodType
assert type(C.f) is types.UnboundMethodType

# Test types.ModuleType
assert type(types) is types.ModuleType

# Test types.InstanceType
assert type(C()) is types.InstanceType

# Test types.LambdaType
assert type((lambda x:x)) is types.LambdaType

# Test types.ListType
assert type([]) is types.ListType

# Test types.TupleType
assert type(()) is types.TupleType

# Test types.DictType
assert type({}) is types.DictType

# Test types.StringType
assert type
