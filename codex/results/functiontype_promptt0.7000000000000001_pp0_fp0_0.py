import types
# Test types.FunctionType
def test_function():
    def f(x):
        return x + 2
    assert f(1) == 3
    assert type(f) == types.FunctionType

# Test types.LambdaType
def test_lambda():
    f = lambda x: x + 2
    assert f(1) == 3
    assert type(f) == types.LambdaType

# Test types.GeneratorType
def test_generator():
    def f(x):
        for i in range(x):
            yield i
    g = f(4)
    assert type(g) == types.GeneratorType
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 3
    try:
        next(g)
    except StopIteration:
        pass

# Test types.GeneratorType (again)
def test_generator_expr():
    g = (x for x in range(4))
    assert type(g) == types.GeneratorType
    assert next(g
