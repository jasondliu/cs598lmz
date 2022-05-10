import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(test_builtin_function_type, types.BuiltinFunctionType)

# Test types.LambdaType
lambda_func = lambda x: x
assert isinstance(lambda_func, types.LambdaType)

# Test types.GeneratorType
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
assert isinstance(fib(1), types.GeneratorType)

# Test types.GeneratorType
def test_generator_type():
    for x in fib(1):
        assert isinstance(x, types.GeneratorType)

# Test types.GeneratorType
class Fib:
    def __init__(self, max):
        self.max = max
        self.n, self
