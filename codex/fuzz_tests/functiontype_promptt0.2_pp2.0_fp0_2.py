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
print(type(Hello.hello) == types.FunctionType)

# Test types.BuiltinMethodType
print(type(str.lower) == types.BuiltinMethodType)

# Test types.ModuleType
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception('hello, world!')
except Exception as e:
    print(type(e.__traceback__) == types.TracebackType
