import types
# Test types.FunctionType
def testFunctionType(x):
    return x

print(type(testFunctionType))
print(type(testFunctionType) == types.FunctionType)

# Test types.LambdaType
testLambdaType = lambda x: x
print(type(testLambdaType))
print(type(testLambdaType) == types.LambdaType)

# Test types.GeneratorType
def testGeneratorType():
    yield 1

print(type(testGeneratorType))
print(type(testGeneratorType()) == types.GeneratorType)

# Test types.CodeType
print(type(testFunctionType.__code__) == types.CodeType)
print(type(testLambdaType.__code__) == types.CodeType)
print(type(testGeneratorType.__code__) == types.CodeType)

# Test types.MethodType
class TestMethodType(object):
    @staticmethod
    def testMethodType(x):
        return x

print(type(TestMethodType.testMethodType))
print(
