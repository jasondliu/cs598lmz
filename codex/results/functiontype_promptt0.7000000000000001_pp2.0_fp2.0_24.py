import types
# Test types.FunctionType function

class TestFunctionType():

    def test_function_type_name(self):
        assert "FunctionType" == types.FunctionType.__name__
