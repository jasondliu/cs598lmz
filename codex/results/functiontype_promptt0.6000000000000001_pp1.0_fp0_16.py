import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
print(type(h.hello) == types.MethodType)

# Test types.UnboundMethodType
print(type(Hello.hello) == types.UnboundMethodType)


# Test types.InstanceType

# Test types.ClassType

# Test types.TypeType
print(type(Hello) == types.TypeType)
print(type(int) == types.TypeType)
print(type(Hello) == type(int))
print(type(Hello) == types.TypeType)

# Test types.NoneType

# Test types.NotImplementedType


