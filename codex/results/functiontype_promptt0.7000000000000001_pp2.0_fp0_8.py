import types
# Test types.FunctionType.
def test_types_function_type(i):
    def test(i):
        return i
    assert type(test) == types.FunctionType

# Test types.LambdaType.
def test_types_lambda_type(i):
    test = lambda i: i
    assert type(test) == types.LambdaType
