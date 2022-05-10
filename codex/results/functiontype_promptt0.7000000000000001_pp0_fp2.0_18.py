import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)
    assert isinstance(test_generator_type, types.FunctionType)
    assert isinstance(test_coroutine_type, types.FunctionType)
    assert isinstance(test_coroutine_type, types.FunctionType)
    assert not isinstance(test_fibonacci_yield, types.FunctionType)
    assert not isinstance(test_fibonacci_yield, types.FunctionType)
    assert not isinstance(test_fibonacci_await, types.FunctionType)
    assert not isinstance(test_fibonacci_await, types.FunctionType)
    assert not isinstance(test_fibonacci_yield_from, types.FunctionType)
    assert not isinstance(test_fibonacci_yield_from, types.FunctionType)
    assert not isinstance(test_fibonacci, types.FunctionType)
    assert not isinstance(test_fibonacci, types.FunctionType)


