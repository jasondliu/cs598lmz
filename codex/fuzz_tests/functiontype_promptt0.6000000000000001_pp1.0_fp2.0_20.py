import types
# Test types.FunctionType
def fun(a):
    return a
print(type(fun) is types.FunctionType)
print(type(abs) is types.BuiltinFunctionType)
print(type(lambda x: x) is types.LambdaType)
print(type((x for x in range(10))) is types.GeneratorType)
# Test types.MemberDescriptorType
class Test(object):
    def __init__(self, a):
        self.a = a

print(type(Test.a) is types.MemberDescriptorType)
print(type(Test.__init__) is types.MethodDescriptorType)
# Test types.UnboundMethodType
class Test(object):
    def test(self, a):
        return a
print(type(Test.test) is types.UnboundMethodType)
print(type(Test().test) is types.MethodType)
