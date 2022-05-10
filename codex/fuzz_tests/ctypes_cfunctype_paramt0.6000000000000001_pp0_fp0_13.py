import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class Test(unittest.TestCase):

    def test_create_function_type(self):
        # Test that a function type can be created.
        self.assertIsInstance(ctypes.CFUNCTYPE(ctypes.c_int), FUNTYPE)

    def test_call(self):
        # Test that a function type can be called.
        func = FUNTYPE(lambda: 42)
        self.assertEqual(func(), 42)

    def test_call_with_args(self):
        # Test that a function type can be called with arguments.
        func = FUNTYPE(lambda x, y: x - y)
        self.assertEqual(func(1, 2), -1)

    def test_call_with_keywords(self):
        # Test that a function type can be called with keyword arguments.
        func = FUNTYPE(lambda x, y: x - y)
        self.assertEqual(func(y=2, x=1), -1)

    def test_call_with_too_few_args
