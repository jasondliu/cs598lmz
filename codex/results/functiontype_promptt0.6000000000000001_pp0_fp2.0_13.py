import types
# Test types.FunctionType
def my_function():
    pass
print type(my_function)
print type(my_function) == types.FunctionType

# Test types.LambdaType
print type(lambda x: x * x)
print type(lambda x: x * x) == types.LambdaType

# Test types.BuiltinFunctionType
print type(len)
print type(len) == types.BuiltinFunctionType

# Test types.MethodType
class Test(object):
    def test_method(self):
        pass
print type(Test.test_method)
print type(Test.test_method) == types.MethodType

# Test types.UnboundMethodType
print type(Test.test_method) == types.UnboundMethodType

# Test types.ModuleType
print type(math)
print type(math) == types.ModuleType

# Test types.ClassType
print type(Test)
print type(Test) == types.ClassType

# Test types.InstanceType
print type(Test())
print type(Test()) == types.InstanceType

# Test
