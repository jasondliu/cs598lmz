import types
types.MethodType(lambda self: None, None)

class TestClass(object):
    def test_method(self):
        pass


def test_1():
    TestClass.test_method = lambda self: None
    assert TestClass.test_method.__name__ == '<lambda>'
    assert TestClass.test_method.__doc__ is None


def test_2():
    TestClass.test_method = types.MethodType(lambda self: None, None)
    assert TestClass.test_method.__name__ == '<lambda>'
    assert TestClass.test_method.__doc__ is None
