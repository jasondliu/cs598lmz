import types
# Test types.FunctionType
def func(x, y):
    return x + y

print(type(func))
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
import types
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(type(h.hello))
print(type(h.hello) == types.MethodType)

# Test types.UnboundMethodType
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
print(type(Hello.hello))
print(type(Hello.hello) == types.UnboundMethodType)

# Test types.BuiltinMethod
