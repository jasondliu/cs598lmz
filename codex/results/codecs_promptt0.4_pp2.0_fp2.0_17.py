import codecs
# Test codecs.register_error

import test_support
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode_errorhandler(exception):
            if isinstance(exception, UnicodeDecodeError):
                return (u'\ufffd', exception.end)
            raise exception
        codecs.register_error("bad_decode", bad_decode_errorhandler)
        s = '\xff'
        self.assertEqual(s.decode("ascii", "bad_decode"), u'\ufffd')

        def bad_encode_errorhandler(exception):
            if isinstance(exception, UnicodeEncodeError):
                return (u'\ufffd', exception.end)
            raise exception
        codecs.register_error("bad_encode", bad_encode_errorhandler)
        u = u'\u1234'
        self.assertEqual(u.encode("ascii", "bad_encode"), u'
