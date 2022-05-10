import types
# Test types.FunctionType
def f():
    pass
print isinstance(f, types.FunctionType)
# Test types.MethodType
class A(object):
    def f(self):
        pass
a = A()
print isinstance(a.f, types.MethodType)
# Test types.LambdaType
l = lambda: None
print isinstance(l, types.LambdaType)
# Test types.GeneratorType
g = (x for x in xrange(5))
print isinstance(g, types.GeneratorType)
# Test types.BuiltinFunctionType
print isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print isinstance([].append, types.BuiltinMethodType)
# Test types.GetSetDescriptorType
print isinstance(A.f, types.GetSetDescriptorType)
# Test types.MemberDescriptorType
print isinstance(A.__dict__['f'], types.MemberDescriptorType)
# Test types.TracebackType
import sys
try:
    raise Exception()
except:
