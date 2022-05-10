import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x: x, types.LambdaType)
# Test types.CodeType
assert isinstance((lambda x: x).__code__, types.CodeType)
# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A.f, types.MethodType)
# Test types.GeneratorType
assert isinstance((lambda x: (yield x))(3), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.GetSetDescriptorType
assert isinstance(A.f, types.GetSetDescriptorType)
# Test types.MemberDescriptorType
assert isinstance(A.
