import types
# Test types.FunctionType

def test_function_type():
    def f(x): return x
    assert isinstance(f, types.FunctionType)
