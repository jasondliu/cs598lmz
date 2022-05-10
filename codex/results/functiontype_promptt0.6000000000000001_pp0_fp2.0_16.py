import types
# Test types.FunctionType
def test(x):
    print x

print type(test)
print type(test) == types.FunctionType

# Test types.LambdaType
print type((lambda x:x))
print type((lambda x:x)) == types.LambdaType

# Test types.BuiltinFunctionType
print type(len)
print type(len) == types.BuiltinFunctionType

# Test types.MethodType
class A(object):
    def test(self):
        print "class A"

a = A()
print type(a.test)
print type(a.test) == types.MethodType
