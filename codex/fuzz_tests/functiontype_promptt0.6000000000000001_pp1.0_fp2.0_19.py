import types
# Test types.FunctionType
def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x-1)

assert isinstance(f, types.FunctionType)
assert f(5) == 120

# Test types.BuiltinFunctionType
assert isinstance(sum, types.BuiltinFunctionType)
assert sum((1, 2, 3, 4)) == 10

# Test types.MethodType
class TestClass:
    def test_method(self):
        return self.value

assert isinstance(TestClass().test_method, types.MethodType)

# Test types.LambdaType
assert isinstance((lambda x: x * x), types.LambdaType)
assert (lambda x: x * x)(5) == 25

# Test types.GeneratorType
def g(x):
    for i in range(x):
        yield i

assert isinstance(g, types.FunctionType)
assert isinstance(g(5), types.GeneratorType)
assert sum(g(5)) == 10

# Test types.CodeType

