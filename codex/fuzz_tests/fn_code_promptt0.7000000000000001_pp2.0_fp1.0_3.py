fn = lambda: None
# Test fn.__code__ for Python >= 3.4
try:
    hasattr(fn.__code__, 'co_firstlineno')
except AttributeError:
    has_code = False
else:
    has_code = True

if has_code:
    def get_func_code(func, **kwargs):
        code = func.__code__
        return code.co_argcount, code.co_firstlineno, code.co_filename
else:
    def get_func_code(func, **kwargs):
        return func.func_code.co_argcount, func.func_code.co_firstlineno, func.func_code.co_filename

class Test_get_func_code(unittest.TestCase):

    def test_get_func_code_on_function(self):
        self.assertEqual(get_func_code(test_fn), (3, 3, __file__))

    def test_get_func_code_on_lambda(self):
        self.assertEqual(get_func_code(lambda a, b,
