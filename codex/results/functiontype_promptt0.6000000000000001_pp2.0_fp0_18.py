import types
# Test types.FunctionType
def f():
    return 1

assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.MethodType
assert type(f.__call__) == types.MethodType
assert type(f.__doc__) == types.MethodType

# Test types.SimpleNamespace
ns = types.SimpleNamespace()
assert type(ns) == types.SimpleNamespace

# Test types.DynamicClassAttribute
assert type(types.DynamicClassAttribute) == types.DynamicClassAttribute

# Test types.MappingProxyType
d = {'a': 1}
assert type(types.MappingProxyType(d)) == types.MappingProxyType

# Test types.MemberDescriptorType
assert type(int.numerator) == types.MemberDescriptorType

# Test types.GetSetDescriptorType
assert type(int.__dict__) == types.GetSetDescriptorType

# Test types.WrapperDescriptorType
assert type(int.__add
