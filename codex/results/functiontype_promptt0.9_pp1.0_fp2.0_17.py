import types
# Test types.FunctionType == types.BuiltinFunctionType

def Test(tester):

    test = TestClass()

    tester.startGroup("Testing function creation")
    tester.startTest("Functions are Python objects")
    tester.compare(1, 1)
    tester.testDone()

    tester.startTest("Python function is an instanceof FunctionType")
    tester.compare(type(test.func), types.FunctionType)
    tester.testDone()

    tester.startTest("Functions can be called")
    tester.compare(test.func(), 5)
    tester.testDone()

    tester.startTest("built-in functions are an instanceof BuiltinFunctionType")
    tester.compare(type(len), types.BuiltinFunctionType)
    tester.testDone()

    tester.startTest("built-in functions can be called")
    tester.compare(len([1, 2, 3]), 3)
    tester.testDone()

    tester.startTest("Functions can be called with positional arguments")
