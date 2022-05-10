fn = lambda: None
# Test fn.__code__ and the like
test_fn.__code__
test_fn.__code__.co_filename


class TestClass(object):
    def test_method(self):
        pass

    def __call__(self):
        pass
# Test class.method and the like
TestClass.test_method
TestClass.test_method.__code__
TestClass.test_method.__code__.co_filename

# Test class.__call__ and the like
TestClass()
TestClass.__call__
TestClass.__call__.__code__
TestClass.__call__.__code__.co_filename

# Test class() and the like
TestClass()
TestClass().__call__
TestClass().__call__.__code__
TestClass().__call__.__code__.co_filename

# Test getattr() and the like
getattr(TestClass().__call__, '__code__')
getattr(TestClass().__call__, '__code__').co_filename
