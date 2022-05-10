import types
# Test types.FunctionType
func: types.FunctionType = print
func(1)

# Test types.MethodType
class C:
    def f(self) -> None:
        pass
method: types.MethodType = C.f
method(C())

# Test types.BuiltinFunctionType
# TODO

# Test types.BuiltinMethodType
# TODO

# Test types.LambdaType
# TODO

# Test types.GeneratorType
# TODO

# Test types.CodeType
# TODO

# Test types.TracebackType
# TODO

# Test types.FrameType
# TODO

# Test types.GetSetDescriptorType
# TODO

# Test types.MemberDescriptorType
# TODO

# Test types.WrapperDescriptorType
# TODO

# Test types.MappingProxyType
# TODO

# Test types.SimpleNamespace
# TODO

# Test types.DynamicClassAttribute
# TODO

# Test types.ClassMethodDescriptorType
# TODO

# Test
