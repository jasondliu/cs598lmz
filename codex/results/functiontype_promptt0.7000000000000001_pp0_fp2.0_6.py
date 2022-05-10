import types
# Test types.FunctionType
def test_FunctionType():
    def func():
        "FunctionType"
        pass
    assert type(func) is types.FunctionType
    assert func.__doc__ == "FunctionType"

# Test types.LambdaType
def test_LambdaType():
    def test_lambda():
        "LambdaType"
        f = lambda x: x+1
        assert type(f) is types.LambdaType
        assert f.__doc__ == "LambdaType"

# Test types.GeneratorType
def test_GeneratorType():
    def test_generator():
        "GeneratorType"
        def gen():
            for i in range(4):
                yield i
        g = gen()
        assert type(g) is types.GeneratorType
        assert g.__doc__ == "GeneratorType"

# Test types.CodeType
def test_CodeType():
    def test_code():
        "CodeType"
        def func(x, y):
            return x+y
        assert type(func.__code__
