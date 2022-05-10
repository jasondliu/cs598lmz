import types
# Test types.FunctionType
#
# Class to test for a given method
class TestMethod:
    def __init__(self):
        self.test_passed = 0
        self.test_failed = 0
    def test_with(self, actual_result, expected_result, test_name):
        if actual_result == expected_result:
            print('Test passed: ', test_name)
            self.test_passed += 1
        else:
            print('Test failed: ', test_name)
            self.test_failed += 1

# Test methods
def test_method_1(arg1, arg2):
    return arg1 + arg2
def test_method_2(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

# Constants
TEST_METHOD_TYPE = types.FunctionType
TEST_METHOD_NAME = 'test_method_1'
TEST_METHOD_ARGS = ['arg1', 'arg2']
TEST_METHOD_RETURN = 'arg1 + arg2'
TEST_METHOD_VERBOSE = 'test
