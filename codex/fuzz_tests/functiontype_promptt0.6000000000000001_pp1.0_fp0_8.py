import types
# Test types.FunctionType

def func():
    pass

func_type = types.FunctionType(func.__code__, func.__globals__, func.__name__, func.__defaults__, func.__closure__)

print(func_type())

# Test types.MethodType

class A:
    def __init__(self, value):
        self.value = value
    def method_func(self):
        print(self.value)

a = A(10)
method = a.method_func

method_type = types.MethodType(method.__func__, a)

method_type()

# Test types.BuiltinMethodType

print(type(type))

# Test types.BuiltinFunctionType

print(type(print))

# Test types.LambdaType

lambda_type = types.LambdaType(lambda: print("hello"), globals(), "lambda_type", (), ())

lambda_type()

# Test types.GeneratorType

def generator():
    yield 1
    yield 2

gener
