import types
# Test types.FunctionType
f = lambda x: x
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
f = lambda x: x
gen = (x for x in [1, 2, 3])
assert isinstance(gen, types.GeneratorType)
# Test types.CodeType
# Test types.TracebackType
# Test types.FrameType
# Test types.BufferType
# Test types.DictProxyType
# Test types.NotImplementedType
# Test types.EllipsisType
# Test types.GetSetDescriptorType
# Test types.MemberDescriptorType
# Test types.WrapperDescriptorType

# Test types.MethodType
# Test types.BuiltinFunctionType
# Test types.BuiltinMethodType
# Test types.ModuleType
# Test types.FileType
# Test types.XRangeType
# Test types.SliceType
# Test types.EllipsisType
# Test types.Traceback
