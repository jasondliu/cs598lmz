import types
# Test types.FunctionType

def f(x):
    return x + 1

assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)

# Test types.BuiltinFunctionType

assert isinstance(abs, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, types.FunctionType)


# Test other types

# These are all the types (useful for checking the output of type()):
# assert types.ModuleType
# assert types.MethodType
# assert types.BuiltinMethodType
# assert types.WrapperDescriptorType
# assert types.MethodWrapperType
# assert types.ClassMethodDescriptorType
# assert types.MemberDescriptorType
# assert types.GetSetDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert types.MemberDescriptorType
# assert
