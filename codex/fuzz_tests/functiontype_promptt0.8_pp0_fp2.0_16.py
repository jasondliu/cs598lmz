import types
# Test types.FunctionType()
def f(x):
    return x
print type(f) == types.FunctionType
print type(f) == types.InstanceType
# Test types.MethodType()
class C(object):
    def f(self, x):
        return x

c = C()
print type(c.f) == types.MethodType
print type(c.f) == types.FunctionType

# Test types.BuiltinMethodType()
print type(1).__add__ == types.BuiltinMethodType
print type(1).__add__ == types.MethodType

# Test types.UnboundMethodType()
print type(C.f) == types.UnboundMethodType
print type(C.f) == types.MethodType

# Test types.LambdaType()
l = lambda x: x
print type(l) == types.LambdaType
print type(l) == types.FunctionType
print type(1).__abs__ == types.BuiltinFunctionType

# Test types.GetSetDescriptorType()
class C(object):
    def geta(
