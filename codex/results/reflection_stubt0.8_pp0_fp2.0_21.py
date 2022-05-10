fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class ExceptionHandlingSuite(unittest.TestCase):
    """Test that C exceptions are properly marshalled to Python exceptions."""

    def run_and_check(self, fn, *args):
        """Run a function and check that it raises an exception.

        The function must raise an exception. The type of the exception
        must be an exception derived from BaseException. Otherwise
        an AssertionError is raised.

        fn: a callable.
        args: the positional arguments to fn.

        Return the exception instance.
        """
        try:
            fn(*args)
        except Exception as e:
            self.assertIsInstance(e, BaseException)
            return e
        else:
            raise AssertionError('%s(*%s) did not raise' % (fn, args))

    def test_SystemError(self):
        # issue #6130: SystemError shouldn't be raised
        self.assertRaises(ValueError, C.variadic_function, 1)

    def test_ArithmeticError(self):
        # http://bugs.python.org
