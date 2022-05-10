import types
# Test types.FunctionType
def main ():
    print("Test types.FunctionType")
    is_types_functiontype = isinstance(main, types.FunctionType)
    assert is_types_functiontype == True, "main is not types.FunctionType"
    # Test types.GeneratorType
    print("Test types.GeneratorType")
    def yield_test():
        yield 1
    is_types_generatortype = isinstance(yield_test(), types.GeneratorType)
    assert is_types_generatortype == True, "yield_test is not types.GeneratorType"
    # Test types.CodeType
    print("Test types.CodeType")
    is_types_codetype = isinstance(main.__code__, types.CodeType)
    assert is_types_codetype == True, "main.__code__ is not types.CodeType"
    # Test types.LambdaType
    print("Test types.LambdaType")
    def lambda_test():
        return lambda: 1
    is_types_lambdatype = isinstance(
