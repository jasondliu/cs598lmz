import codecs
# Test codecs.register_error("ignore")
from test import test_support

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # bug 7147: codecs.register_error("ignore") should work
        # on non-standard exceptions
        #
        # XXX: This test is not really good...
        class MyException(Exception):
            def __init__(self, start, end, reason):
                self.start = start
                self.end = end
                self.reason = reason

        def my_exc_handler(exc):
            if not isinstance(exc, MyException):
                raise TypeError("don't know how to handle %r" % exc)
            return (u"\ufffd", exc.start + 1)

        codecs.register_error("my.exception", my_exc_handler)
        self.assertEqual(u"abc\ufffdef", u"abc\x80def".decode("ascii", "my.exception"))
        self.assertEqual(u"abc\ufffdef", u"abc\x
