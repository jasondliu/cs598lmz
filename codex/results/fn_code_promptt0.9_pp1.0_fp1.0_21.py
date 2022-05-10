fn = lambda: None
# Test fn.__code__.co_varnames
class TestFunctionGetArguments(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(function_arguments(fn), [])
    def test_no_arg_default(self):
        fn.__defaults__ = (0,)
        self.assertEqual(function_arguments(fn), [])
    def test_no_arg_kwdefault(self):
        fn.__kwdefaults__ = {'hi': 2}
        self.assertEqual(function_arguments(fn), [])
    def test_one_arg(self):
        def fn(a): pass
        self.assertEqual(function_arguments(fn), ['a'])
    def test_one_arg_default(self):
        def fn(a=1): pass
        self.assertEqual(function_arguments(fn), ['a=1'])
    def test_one_arg_default_constant(self):
        def fn(a=1): pass
        self.assertEqual(function
