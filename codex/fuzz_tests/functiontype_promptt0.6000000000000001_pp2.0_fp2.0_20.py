import types
# Test types.FunctionType
def test_type_function():
    def foo(): pass
    f = types.FunctionType(foo.__code__, globals())
    assert f() == None

# Test types.GeneratorType
def test_type_generator():
    def foo():
        yield 1
    g = foo()
    assert type(g) == types.GeneratorType

# Test types.LambdaType
def test_type_lambda():
    l = lambda x: x + 1
    assert type(l) == types.LambdaType
    assert l(1) == 2

# Test types.TracebackType
def test_type_traceback():
    try:
        1/0
    except ZeroDivisionError:
        import sys
        tb = sys.exc_info()[2]
        assert type(tb) == types.TracebackType

# Test types.CodeType
def test_type_code():
    # Function code
    def foo(): pass
    assert type(foo.__code__) == types.CodeType

    # Lambda code

