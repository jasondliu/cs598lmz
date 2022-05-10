import types
# Test types.FunctionType(), types.LambdaType() and types.CodeType()
def test_func(a, b):
    pass

lambda_func = lambda a: a

assert isinstance(test_func, types.FunctionType)
assert isinstance(lambda_func, types.LambdaType)
assert isinstance(test_func.__code__, types.CodeType)
assert isinstance(lambda_func.__code__, types.CodeType)

# Test types.GeneratorType()
def test_generator():
    yield 1

gen = test_generator()
assert isinstance(gen, types.GeneratorType)

# Test types.BuiltinFunctionType() and types.BuiltinMethodType()
import math

assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(math.sin, types.BuiltinFunctionType)
assert isinstance(gen.__iter__, types.BuiltinMethodType)

# Test types.MethodType()
class TestClass:
    def test_method(self):
        pass

assert isinstance(TestClass.test_
