fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 256


class TestCode(unittest.TestCase):
    def test_new_code(self):
        self.assertEqual(CodeType.__new__(CodeType), None)
        self.assertIsInstance(CodeType(), CodeType)

    def test_code_co_argcount(self):
        fn = lambda one, two, three: None
        # Test fn.__code__.co_argcount
        self.assertEqual(fn.__code__.co_argcount, 3)
        with self.assertRaises(AttributeError):
            del fn.__code__.co_argcount
        with self.assertRaises(TypeError):
            fn.__code__.co_argcount = 'string'
        with self.assertRaises(TypeError):
            fn.__code__.co_argcount = 10.5
        with self.assertRaises(ValueError):
            fn.__code__.co_argcount = -1

    def test_code_co_kw
