import types
# Test types.FunctionType and types.LambdaType
tFunctionType = types.FunctionType
def f(x): return x # test f is a standard function
tLambdaType = type(f)
def f(): return f # test f is a lambda function
tLambdaType = type(f)

# Test types.GeneratorType
def g(): yield g
tGeneratorType = type(g())

try:
    # Test types.GetSetDescriptorType
    class C(object):
        def delname(self): pass
    tGetSetDescriptorType = type(C.delname)
    assert tGetSetDescriptorType is types.GetSetDescriptorType
except AttributeError:
    tGetSetDescriptorType = None

try:
    # Test types.MemberDescriptorType
    class C(object):
        name = 1
    tMemberDescriptorType = type(C.name)
    assert tMemberDescriptorType is types.MemberDescriptorType
except AttributeError:
    tMemberDescriptorType = None

# Test
