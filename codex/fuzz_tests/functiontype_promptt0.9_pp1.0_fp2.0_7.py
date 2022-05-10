import types
# Test types.FunctionType
a = types.FunctionType
# Test types.GetSetDescriptorType
a = types.GetSetDescriptorType
# Test types.LambdaType
a = types.LambdaType
# Test types.MappingProxyType
a = types.MappingProxyType
# Test types.MemberDescriptorType
dct = {'five': 5}
a = types.MemberDescriptorType(dct['five'].__get__, None, dct)
# Test types.MethodType
a = types.MethodType
# Test types.ModuleType
a = types.ModuleType
# Test types.TracebackType
a = types.TracebackType
# Test types.WrapperDescriptorType
a = types.WrapperDescriptorType
# Test types.builtin_function_or_method
a = types.builtin_function_or_method
# Test types.code
a = types.code
# Test types.frame
a = types.frame
# Test types.function
class A:
    def __init__(self):
        self.f = lambda
