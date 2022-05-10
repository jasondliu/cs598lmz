import types
# Test types.FunctionType
def fun(x):
    return x*x

print(type(fun)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance(fun, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance((x for x in range(10)), types.GeneratorType))

# Test types.MethodType
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()
print(type(Hello.hello)==types.FunctionType)
print(type(h.hello)==types.MethodType)

print(isinstance(Hello.hello, types.FunctionType))
print(isinstance(h.hello, types.MethodType
