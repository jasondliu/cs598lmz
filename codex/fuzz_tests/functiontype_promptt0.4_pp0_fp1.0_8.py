import types
# Test types.FunctionType
def func(x):
    return x

print type(func) == types.FunctionType

# Test types.LambdaType
lambda_func = lambda x: x
print type(lambda_func) == types.LambdaType

# Test types.GeneratorType
def gen_func():
    for i in range(10):
        yield i

gen = gen_func()
print type(gen) == types.GeneratorType

# Test types.BuiltinFunctionType
print type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A(object):
    def hello(self):
        return 'Hello, world!'

a = A()
print type(a.hello) == types.MethodType

# Test types.UnboundMethodType
print type(A.hello) == types.UnboundMethodType

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.exc_info
