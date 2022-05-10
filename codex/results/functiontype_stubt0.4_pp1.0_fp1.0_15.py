from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    pass

print(type(a))
print(type(a) == FunctionType)

print(type(a) == types.GeneratorType)
print(type(a) == types.FunctionType)

print(type(a) == types.LambdaType)
print(type(a) == types.BuiltinFunctionType)

print(type(a) == types.BuiltinMethodType)
print(type(a) == types.MethodType)
print(type(a) == types.ModuleType)
print(type(a) == types.TracebackType)

print(type(a) == types.FrameType)
print(type(a) == types.CodeType)

print(type(a) == types.MappingProxyType)
print(type(a) == types.SimpleNamespace)
print(type(a) == types.DynamicClassAttribute)
print(type(a) == types.MemberDescriptorType)

print(type(a) == types.GetSetDescriptorType)
