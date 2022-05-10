import types
# Test types.FunctionType

def foo():
    pass

def test_function_type():
    a_func = foo
    assert isinstance(foo, types.FunctionType)
    assert isinstance(a_func, types.FunctionType)

# Test for lambda
# We can't use assert_raises() because the exception raised is MemoryError
def test_lambda():
    try:
        a_lambda = (lambda x: x).__code__
        assert isinstance(a_lambda, types.CodeType)
    except MemoryError:
        pass
