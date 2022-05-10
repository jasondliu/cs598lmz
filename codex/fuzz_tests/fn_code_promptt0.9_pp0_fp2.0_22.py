fn = lambda: None
# Test fn.__code__.co_filename. Using this filename instead of the first line
# of the test fn.__doc__ because the filename is much more obvious and stable
# than the docstring of the test function.
test_fn.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), "", "fn", 1, b"")
test_fn.__code__.co_filename = __file__
test_fn._test_file = __file__


class MockEntry(object):
    def __init__(self, name):
        self.name = name
        self.type = "regular"
        self.mode = 0o755
        self.mtime = 0
        self.path = os.path.join("dir", name)


class BaseTests(unittest.TestCase):
    def test_add_test(self):
        test1 = test_fn
        test1.__doc__ = 'amazing test'
        test2 = test_fn
        suite = unittest2.TestSuite()
        suite.addTest(test1)
