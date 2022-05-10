import types
# Test types.FunctionType vs types.MethodType

def func(): pass

class C:
    def meth(): pass

assert type(func) is types.FunctionType
assert type(C.meth) is types.MethodType
assert type(C().meth) is types.MethodType

# Test for issue #14630
assert types.MethodType.__qualified__ is types.MethodType
assert types.CodeType.__qualified__ is types.CodeType
assert types.FrameType.__qualified__ is types.FrameType
assert types.TracebackType.__qualified__ is types.TracebackType
assert types.GetSetDescriptorType.__qualified__ is types.GetSetDescriptorType
assert types.MemberDescriptorType.__qualified__ is types.MemberDescriptorType
assert types.WrapperDescriptorType.__qualified__ is types.WrapperDescriptorType
assert types.FunctionType.__qualified__ is types.FunctionType
