import types
# Test types.FunctionType
def f1(x):
    print "Welcome", x
print type(f1)
print type(f1) == types.FunctionType
print type(f1) == types.InstanceType
print type(f1) == types.DictType
print type(f1) == types.IntType
print type(f1) == types.StringType
print type(f1) == types.NoneType
print type(f1) == types.UnicodeType
print type(f1) == type(lambda x: x)
print type(f1) == type(lambda x: x) == types.LambdaType
# Test types.GeneratorType
def f2():
    for i in range(10):
        yield i*i
print type(f2) == types.FunctionType # should be True
print type(f2()) == types.GeneratorType # should be True
# Test types.UnboundMethodType
class A:
    def f3(self, x):
        print "Welcome", x
print type(A.f3) == types.UnboundMethodType
# Test
