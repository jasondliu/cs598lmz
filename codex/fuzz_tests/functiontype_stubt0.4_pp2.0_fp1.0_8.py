from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    pass

print(type(f))
print(type(f()) == type(None))
print(type(f) == FunctionType)

import types
print(type(f) == types.GeneratorType)
print(type(f) == types.FunctionType)

print(type(f) == types.BuiltinFunctionType)
print(type(f) == types.BuiltinMethodType)
print(type(f) == types.MethodType)

print(type(f) == types.LambdaType)
print(type(f) == types.UnboundMethodType)

print(type(f) == types.ModuleType)
print(type(f) == types.TracebackType)
print(type(f) == types.FrameType)
print(type(f) == types.CodeType)
print(type(f) == types.GetSetDescriptorType)
print(type(f) == types.MemberDescriptorType)
print(type(f) == types.WrapperDescriptor
