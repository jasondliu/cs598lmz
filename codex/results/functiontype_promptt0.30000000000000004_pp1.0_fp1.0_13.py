import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.ClassType
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
print(type(Hello) == types.ClassType)
print(type(Hello) == type)

# Test types.InstanceType
h = Hello()
print(type(h) == types.InstanceType)
print(type(h) == type)

# Test types.UnboundMethodType
print(type(Hello.hello) == types.UnboundMethodType)

# Test types.MethodType
print(type(h.hello) == types.MethodType)

# Test types.BuiltinMethodType
print(type(str.replace) == types.BuiltinMethodType)

# Test types.ModuleType
