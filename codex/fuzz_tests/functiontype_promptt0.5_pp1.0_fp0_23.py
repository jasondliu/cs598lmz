import types
# Test types.FunctionType
def foo(x):
    return x + 1

def bar(y):
    return y - 1

print(type(foo))
print(foo(10))
print(type(bar))
print(bar(10))

# Test types.LambdaType
lambda_foo = lambda x: x + 1
lambda_bar = lambda y: y - 1

print(type(lambda_foo))
print(lambda_foo(10))
print(type(lambda_bar))
print(lambda_bar(10))

# Test types.BuiltinFunctionType
print(type(sum))
print(sum([1, 2, 3]))
print(type(print))
print(print('hello'))

# Test types.BuiltinMethodType
print(type(str.upper))
print(str.upper('hello'))
print(type(str.join))
print(str.join('-', ['hello', 'world']))

# Test types.MethodType
class Test(object):
    def __init__(self):
        pass

    def hello(self):

