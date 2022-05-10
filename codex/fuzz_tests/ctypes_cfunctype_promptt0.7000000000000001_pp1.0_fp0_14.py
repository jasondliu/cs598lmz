import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_int)

@contextlib.contextmanager
def assert_raises_os_error(testcase, errno):
    try:
        yield
    except OSError as e:
        testcase.assertEqual(e.errno, errno)
    else:
        testcase.fail("Expected OSError(%d) to be raised" % errno)

class Test_CFUNCTYPE(unittest.TestCase):
    def test_CFUNCTYPE_errcheck(self):
        # This function returns -1, which is the C convention for
        # returning an error from a function.  If this error is
        # reported to Python as such, it will cause a SystemError to
        # be raised.  The errcheck function converts this to a
        # OSError, which is what the Python API would do.
        #
        # The CFUNCTYPE takes two parameters.  The first one isn't
        # used by the errcheck function, and the second is the
        # return value of the C
