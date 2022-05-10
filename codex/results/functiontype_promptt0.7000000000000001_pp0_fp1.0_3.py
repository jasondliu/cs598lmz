import types
# Test types.FunctionType
assert type(test_function) == types.FunctionType
# Test __name__
assert test_function.__name__ == 'test_function'
# Test __doc__
assert test_function.__doc__ == 'A test function'
# Test __module__
assert test_function.__module__ == __name__
# Test __annotations__
assert test_function.__annotations__ == {'x': <class 'int'>}

# Test __call__
assert test_function(1) == 2
# Test TypeError
try:
    test_function(1.5)
    assert False
except TypeError:
    pass

# Create a test object
class TestObject:
    @staticmethod
    def test_method(x: int) -> int:
        '''A test method'''
        return x + 1

# Test __get__
assert TestObject.test_method.__get__(1) == types.MethodType(TestObject.test_method, 1)
# Test __set__
try:
    TestObject.test_method.__set__(1
