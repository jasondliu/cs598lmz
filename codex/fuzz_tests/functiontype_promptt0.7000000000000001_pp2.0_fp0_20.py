import types
# Test types.FunctionType()
def test_function_type(tester):
    tester.startGroup("FunctionType")
    import _testcapi
    # tester.startTest("FunctionType")
    test_values = [
        lambda x: x,
        _testcapi.make_exception,
        types.FunctionType,
        ]
    for item in test_values:
        tester.startTest(repr(item))
        try:
            test_target = types.FunctionType
        except:
            tester.error("Failed to create FunctionType")
        if not isinstance(item, test_target):
            tester.error("Expected FunctionType, got {0}".format(
                item.__class__.__name__))
        tester.testDone()
    tester.groupDone()


# Test types.GeneratorType()
def test_generator_type(tester):
    tester.startGroup("GeneratorType")
    import _testcapi
    # tester.startTest("GeneratorType")
    test_values = [
       
