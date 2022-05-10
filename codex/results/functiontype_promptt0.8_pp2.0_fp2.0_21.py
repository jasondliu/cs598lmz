import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.MethodType
def f():
    pass
var = f.__get__(None, object)
assert isinstance(var, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(object.__eq__, types.BuiltinMethodType)
# Test types.GeneratorType
def f():
    yield
assert isinstance(f(), types.GeneratorType)
# Test types.AsyncGeneratorType
async def f():
    yield
assert isinstance(f(), types.AsyncGeneratorType)
# Test types.MethodDescriptorType
assert isinstance(type.__repr__, types.MethodDescriptorType)
# Test types.GetSetDescriptorType
assert isinstance(int.imag, types.GetSetDescriptorType)
# Test types.MemberDescriptorType
assert isinstance(int.real, types.MemberDescriptorType)

